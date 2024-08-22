import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes.Post import Post
from Details import Application
import requests

base_ig_url = "https://graph.instagram.com"
base_fb_url = "https://graph.facebook.com"
params = {}
userData = {}
class PostPublishingService:
    # Singleton design pattern in python.
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
        print("Getting user details...")
        params["access_token"] = Application.keys["instagram_app_user_access_token"]
        params["fields"] = ["user_id,username,account_type,name"]
        response = requests.get(base_ig_url + f"/me", params)
        userData = response.json()
        params["fields"] = None
        print(f"Username: {userData['username']}. User id: {userData['user_id']}\n")

        return userData
    
    def createMediaContainer(self, userId, post:Post):
        print(f"Creating media container...")
        print(f"Post image url: {post.image}")
        print(f"Post caption: {post.text}")
        params["access_token"] = Application.keys["instagram_app_user_access_token"]
        params["image_url"] = post.image
        params["caption"] = post.text
        response = requests.post(base_ig_url + f"/{userId}/media", params)
        containerId = response.json()["id"]
        params["image_url"] = None
        params["caption"] = None
        print(f"Post created, container id: {containerId}\n")
        
        return containerId

    def publishMediaContainer(self, userId, containerId):
        print(f"Publishing post...")
        params["access_token"] = Application.keys["facebook_page_user_access_token"]
        params["creation_id"] = containerId
        response = requests.post(base_fb_url + f"/{userId}/media_publish", params)
        mediaId = response.json()["id"]
        params["creation_id"] = None
        print(f"Post published, media id: {mediaId}\n")

        return mediaId
    
    def getLongLivedAccessToken(self, accessToken):
        url = base_fb_url + '/oauth/access_token'
        param = dict()
        param['grant_type'] = 'fb_exchange_token'
        param['client_id'] = Application.loginInfo["developer_app_id"]
        param['client_secret'] = Application.keys["developer_app_secret_key"]
        param['fb_exchange_token'] = accessToken
        response = requests.get(url = url,params=param)
        long_lived_access_tokken =response.json()["access_token"]

        return long_lived_access_tokken
    
# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()
    if not Application.keys["facebook_page_user_access_token"]:
        shortLivedAccessToken = Application.keys["facebook_page_user_short_lived_access_token"]
        p.getLongLivedAccessToken(shortLivedAccessToken)
    p.publishPost(Post("https://storage.googleapis.com/instagram-autobot-df35b.appspot.com/Post%2310.jpg", "Test"))