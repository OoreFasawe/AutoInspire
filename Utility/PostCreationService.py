import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from openai import OpenAI 
from Classes import Post
from Details import Application
import requests
class PostCreationService(object):
    def __new__(cls):
        # singleton design pattern in python
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostCreationService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        pass
    
    def savePost(self, post: Post):
        pass

creationService = PostCreationService()
creationService.createPost()