import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes import Post
from instabot import Bot

class PostPublishingService:
    # singleton design pattern in python
    def __new__(self,cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
            
        #creating insta bot and logging in here when singleton is created
        self.bot = Bot()
        self.bot.login(username='butterman_32', password='ooreAutobot')
        
        return cls.instance

    def publishPost(self, post:Post):
        #Calling upload here
        self.bot.upload_photo(post.imageUrl, caption= post.text)
        
        return