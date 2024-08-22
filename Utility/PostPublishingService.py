import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes.Post import Post
# from instabot.bot import Bot
from Details import Application
import requests
import time

base_ig_url = "https://graph.instagram.com"
base_fb_url = "https://graph.facebook.com"
params = {}
userData = {}
class PostPublishingService:

    # singleton design pattern in python
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
        
        return cls.instance 

    def publishPost(self, post:Post):
        userData = p.getUserDetails()
        userId = userData["user_id"]
        containerId = self.createMediaContainer(userId, post)
        mediaId = p.publishMediaContainer(userId, containerId)

        return mediaId
    
    def getUserDetails(self):
        params["access_token"] = Application.keys["instagram_app_user_access_token"]
        params["fields"] = ["user_id,username,account_type,name"]
        response = requests.get(base_ig_url + f"/me", params)
        userData = response.json()
        params["fields"] = None

        return userData
    
    def createMediaContainer(self, userId, post:Post):
        params["access_token"] = Application.keys["instagram_app_user_access_token"]
        params["image_url"] = post.image
        params["caption"] = post.text
        response = requests.post(base_ig_url + f"/{userId}/media", params)
        containerId = response.json()["id"]
        params["image_url"] = None
        params["caption"] = None

        return containerId

    def publishMediaContainer(self, userId, containerId):
        params["access_token"] = Application.keys["facebook_page_user_access_token"]
        params["creation_id"] = containerId
        response = requests.post(base_fb_url + f"/{userId}/media_publish", params)
        mediaId = response.json()["id"]
        params["creation_id"] = None

        return mediaId
    
# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()
    p.publishPost(Post("https://storage.googleapis.com/instagram-autobot-df35b.appspot.com/Post%2310.jpg", "Test"))