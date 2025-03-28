import os
import logging
from Classes.Post import Post, PostTypes
import requests

base_ig_url = "https://graph.instagram.com/"
base_fb_url = "https://graph.facebook.com/"
params = {}
userData = {}

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=os.environ.get("LOG_LEVEL", "INFO"),
)

class PostPublishingService:
    instagram_access_token = os.environ.get("INSTAGRAM_ACCESS_TOKEN")
    # Singleton design pattern in python.
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
        return cls.instance 

    def publishPost(self, post:Post):
        logging.info("Starting Post Publishing Service")
        post.publishPost(self)
        return
    
    def getUserDetails(self):
        logging.info("Getting Instagram user details...")
        access_token = self.instagram_access_token
        if not access_token:
            logging.error("Instagram access token not found.")
            return None
        params = {
            "access_token": access_token,
            "fields": "user_id,username,account_type,name"
        }
        logging.debug(f"Instagram Access Token, last 5 chars: {access_token[-5:]}")
        try:
            response = requests.get(base_ig_url + "me", params=params)
            response.raise_for_status()  # Raises HTTPError if status is 4xx/5xx
            userData = response.json()
            logging.info(f"Username: {userData.get('username')}. User id: {userData.get('user_id')}\n")
            return userData
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error: {e} - Response: {response.text}")
        except ValueError:
            logging.error(f"Failed to parse JSON from response: {response.text}")
        except Exception as e:
            logging.error(f"Unexpected error fetching user details: {e}")
            
        return dict()
    
    def createMediaContainer(self, userId, post:Post):
        logging.info(f"Creating media container...")
        logging.debug(f"Post media url: {post.mediaUrl}")
        logging.debug(f"Post caption:{post.caption}")
        logging.debug(f"Post hashtags:{post.hashtags}")
        access_token = self.instagram_access_token
        if not access_token:
            logging.error("Instagram access token not found.")
            return None
        params["access_token"] = access_token
        params["is_carousel"] = post.postType == PostTypes.CAROUSEL
        params["caption"] = (post.caption + "\n\n" + post.hashtags) if post.postType != PostTypes.CAROUSEL else None
        containers = []
        for mediaUrl in post.mediaUrl:
            params["image_url"] = mediaUrl
            response = requests.post(base_ig_url + f"{userId}/media", params)
            print(response.json())
            itemContainer = response.json()["id"]
            containers.append(itemContainer)
        params["image_url"] = None
        params["caption"] = None
        logging.info(f"Media containers created, container id: {containers}\n")
        return containers
    
    def createCarouselContainer(self, userId, post:Post, itemContainerIds):
        print(f"Creating carousel container...")
        params["access_token"] = self.instagram_access_token
        params["media_type"] = "CAROUSEL"
        params["children"] = itemContainerIds
        params["caption"] = post.caption + "\n\n" + post.hashtags
        response = requests.post(base_ig_url + f"{userId}/media", json=params)
        carouselContainer = response.json()["id"]
        print(f"Carousel container created, container id: {carouselContainer}\n")
        return carouselContainer

    def publishMediaContainer(self, userId, containerId):
        logging.info(f"Publishing post...")
        params["access_token"] = self.instagram_access_token
        params["creation_id"] = containerId
        response = requests.post(base_ig_url + f"{userId}/media_publish", params)
        mediaId = response.json()["id"]
        params["creation_id"] = None
        logging.info(f"Post published, media id: {mediaId}\n")
        return mediaId
    
# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()
    p.getUserDetails()

