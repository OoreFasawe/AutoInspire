import sys
import os
ABS_PATH = '/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'
sys.path.append(os.path.abspath(ABS_PATH))
from Classes.Post import Post, PostTypes
from Utility.PostPublishingService import PostPublishingService

class ImagePost(Post):
    def __init__(self, fileName=None, mediaUrl=None, caption=None, hashtags=None):
        super().__init__(fileName, mediaUrl, caption, hashtags)
        self.numberOfPosts = 1
        self.postType = PostTypes.IMAGE
    
    def publishPost(self, publishingService: PostPublishingService):
        userData = publishingService.getUserDetails()
        userId = userData["user_id"]
        containerId = publishingService.createMediaContainer(userId, self)[0]
        mediaId = publishingService.publishMediaContainer(userId, containerId)
        return mediaId
        