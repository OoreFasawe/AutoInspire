import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from openai import OpenAI 
from Classes.Post import Post
from Details import Application
import requests
class PostCreationService(object):
    client = OpenAI(api_key=Application.keys["api_secret_key"])
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
        return newPost

    def savePost(self, post: Post):
        pass

    def retrievePreviousPosts(self):
        pass

    def generateText(self):
        #TODO(oore): Add better prompt engineering to generate quotes.
        textCompletion = PostCreationService.client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": "Give me a short quote enough for an Instagram post."}],
        ).to_dict()
        text = textCompletion["choices"][0]["message"]["content"]
        return text
    
    def generateImage(self, text):
        #TODO(oore): Explore better image genetation options. The texts on images being generated aren't accurate.
        imgPrompt = f'Make a picture background with exactly the words "{text}" written on it clearly.'
        imageCompletion = PostCreationService.client.images.generate(
            model="dall-e-3",
            prompt=imgPrompt,
            size="1024x1024",
        ).to_dict()
        imageUrl = imageCompletion["data"][0]["url"]
        return imageUrl