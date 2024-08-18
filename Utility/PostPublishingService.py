import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes.Post import Post
# from instabot.bot import Bot
from Details import Application
import requests

base_url = "https://graph.facebook.com"
params = {"access_token": Application.keys["instagram_access_token"]}
class PostPublishingService:
    # bot =  Bot()
    # bot.login(username=Application.loginInfo["instagram_username"], 
    #           password=Application.loginInfo["instagram_password"])

    # singleton design pattern in python
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
        
        return cls.instance 

    def publishPost(self, post:Post):
        #Calling upload here
        isPostPublished = PostPublishingService.bot.upload_photo(post.image, caption= post.text)
        
        return isPostPublished
    
    def authenticateUser(self):
        response = requests.get(base_url + "/me/accounts", params)
        print(response.json())
        return

# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()
    p.authenticateUser()