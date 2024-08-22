import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes.Post import Post
# from instabot.bot import Bot
from Details import Application
import requests

base_url = "https://graph.instagram.com"
params = {"access_token": {Application.keys["instagram_app_user_access_token"]}}
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
        
        return 
    
    def getUserDetails(self):
        params["fields"] = ["user_id,username,account_type,name"]
        response = requests.get(base_url + f"/me", params)
        userData = response.json()
        params["fields"] = None
        print(userData)
        return userData
    
    def createMediaContainer(self, userId):
        params["image_url"] = "https://storage.googleapis.com/instagram-autobot-df35b.appspot.com/Post%2310.jpg"
        response = requests.get(base_url + f"/{userId}/media", params)
        containerId = response.json()
        print(containerId)
        return containerId

# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()