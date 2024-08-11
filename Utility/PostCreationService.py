import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from openai import OpenAI 
from Classes.Post import Post
from Details import Application
import requests
class PostCreationService(object):
    def __new__(cls):
        # singleton design pattern in python
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostCreationService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        previousPosts = self.retrievePreviousPosts()
        newPost = Post()
        newPost.text = self.generateText()
        newPost.image = self.generateImage()
        return newPost

    def savePost(self, post: Post):
        pass

    def retrievePreviousPosts(self):
        pass

    def generateText(self):
        client = OpenAI(api_key=Application.keys["api_secret_key"])
        #TODO(oore): Add better prompt engineering to generate quotes
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": "Give me a short quote enough for an Instagram post"}],
        ).to_dict()
        text = completion["choices"][0]["message"]["content"]
        return text
    
    def generateImage(self):
        pass

p = PostCreationService()
p.createPost()