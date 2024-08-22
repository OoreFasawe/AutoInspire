import sys
import os
ABS_PATH = '/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'
sys.path.append(os.path.abspath(ABS_PATH))
from openai import OpenAI 
from Classes.Post import Post
from Details import Application
import firebase_admin
from firebase_admin import firestore, credentials, storage
import requests
class PostCreationService(object):
    client = OpenAI(api_key=Application.keys["api_secret_key"])
    cred = credentials.Certificate(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot/firebaseServiceAccount.json'))
    firebase_admin.initialize_app(cred, {"storageBucket": "instagram-autobot-df35b.appspot.com"})
    db = firestore.client()
    bucket = storage.bucket()
    
    def __new__(cls):
        # Singleton design pattern in python.
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostCreationService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        previousPosts = self.retrievePreviousPosts()
        newPost = Post()
        newPost.text = self.generateText()
        newPost.imageUrl = self.generateImage(newPost.text)
        newPost.fileName = self.createFileName()
        return newPost

    def savePost(self, post: Post):
        # save to firebase storage
        print(f"Saving {post.fileName} to database...")
        blob = PostCreationService.bucket.blob(f"{post.fileName}.jpg")
        imageData = requests.get(post.imageUrl).content
        blob.upload_from_string(
            imageData,
            content_type='image/jpg'
        )
        # change temporary url to firebase permanent url and store in database
        post.imageUrl = blob.public_url
        blob.make_public()
        PostCreationService.db.collection("posts").add(document_id=post.fileName, document_data={"document" "text": post.text, "imageUrl": post.imageUrl})
        print(f"Saved {post.fileName} to database. Public url: {post.imageUrl}\n")
        return

    def retrievePreviousPosts(self):
        pass

    def generateText(self):
        #TODO(oore): Add better prompt engineering to generate quotes.
        print("Generating caption...")
        textCompletion = PostCreationService.client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": "Give me a short quote enough for an Instagram post; no hashtags, just a text."}],
        ).to_dict()
        text = textCompletion["choices"][0]["message"]["content"]
        print(f"Caption: {text}\n")
        return text
    
    def generateImage(self, text):
        print("Generating image...")
        #TODO(oore): Explore better image genetation options. The texts on images being generated aren't accurate.
        imgPrompt = f'Make a picture background with exactly the words "{text}" written on it clearly.'
        imageCompletion = PostCreationService.client.images.generate(
            model="dall-e-3",
            prompt=imgPrompt,
            size="1024x1024",
        ).to_dict()
        imageUrl = imageCompletion["data"][0]["url"]
        print(f"Image url: {imageUrl}\n")
        return imageUrl
    
    def createFileName(self):
        print("Creating post file name...")
        postCollection = PostCreationService.db.collection("posts")
        # TODO(oore): Add count variable to database for faster lookup
        countQuery = postCollection.count()
        numberOfPosts = countQuery.get()[0][0].value
        fileName = f"Post#{int(numberOfPosts + 1)}"
        print(f"File name: {fileName}\n")
        return fileName

# demo functionality
if __name__ == "__main__":
    p = PostCreationService()
    newPost = p.createPost()
    p.savePost(newPost)
