import sys
import os
ABS_PATH = '/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'
sys.path.append(os.path.abspath(ABS_PATH))
from Classes.Post import Post, PostTypes
from Utility.PostPublishingService import PostPublishingService

class CarouselPost(Post):
    def __init__(self, fileName=None, mediaUrl=None, caption=None, hashtags=None):
        super.__init__(fileName, mediaUrl, caption, hashtags)
        self.numberOfPosts = 5
        self.postType = PostTypes.CAROUSEL