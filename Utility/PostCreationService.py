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
        newPost.mediaUrl = self.generateImage(newPost.text)
        newPost.fileName = self.createFileName()
        return newPost

    def savePost(self, post: Post):
        # save to firebase storage
        print(f"Saving {post.fileName} to database...")
        blob = PostCreationService.bucket.blob(f"{post.fileName}.jpg")
        imageData = requests.get(post.mediaUrl).content
        blob.upload_from_string(
            imageData,
            content_type='image/jpg'
        )
        # change temporary url to firebase permanent url and store in database
        post.mediaUrl = blob.public_url
        blob.make_public()
        PostCreationService.db.collection("posts").add(document_id=post.fileName, document_data={"document" "text": post.text, "mediaUrl": post.mediaUrl})
        print(f"Saved {post.fileName} to database. Public url: {post.mediaUrl}\n")
        return

    def retrievePreviousPosts(self):
        path = "../Cache/previousPosts.txt"
        postCacheExists = os.path.isfile(path)
        if not postCacheExists:
            try:
                # create new file
                open(path, "x")
                f = open(path, "a")
                for _ in range(20):
                    f.write("xx\n")
                f.close()
            except Exception as error:
                print("file exists but for some reason was not found by system", error)

        # read file content
        f = open(path, "r")
        previousPosts = []
        for _ in range(20):
            line = f.readline().rstrip("xx\n")
            previousPosts.append(line)
        return previousPosts
        
    def generateText(self):
        #TODO(oore): Add better prompt engineering to generate quotes.
        print("Generating caption...")
        textCompletion = PostCreationService.client.chat.completions.create(
            messages=[{"role": "user", "content": "Give me a short quote enough for an Instagram post; no hashtags, just a text."}],
            model="gpt-4o-mini", 
        ).to_dict()
        text = textCompletion["choices"][0]["message"]["content"]
        hashtagCompletion = textCompletion = PostCreationService.client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": f"Make five space-seperated relevant hashtags to this text on a single line):{text}."}],
        ).to_dict()
        hashtags = hashtagCompletion["choices"][0]["message"]["content"]
        caption = "Quote of the day:\n" + text + "\n\n" + "#Motivation " + hashtags
        print(f"Caption: {caption}\n")
        return caption
    
    def generateImage(self, text):
        print("Generating image...")
        #TODO(oore): Explore better image genetation options. The texts on images being generated aren't accurate.
        imgPrompt = f'Make a visual that depicts what is said in this text(no need to add text on the image): "{text}"'
        imageCompletion = PostCreationService.client.images.generate(
            model="dall-e-3",
            prompt=imgPrompt,
            size="1024x1024",
            style="vivid",
        ).to_dict()
        mediaUrl = imageCompletion["data"][0]["url"]
        print(f"Image url: {mediaUrl}\n")
        return mediaUrl
    
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
    print(p.retrievePreviousPosts())
