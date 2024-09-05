from enum import Enum
class PostTypes(Enum):
    NONE = 0
    IMAGE = 1
    VIDEO = 2
    CAROUSEL = 3

from abc import abstractmethod
class Post:
    def __init__(self, fileName=None, mediaUrls=[], caption=None, hashtags=None, postType = PostTypes.NONE):
        # Each post should have a picture and some text
        self.fileName = fileName
        self.mediaUrls = mediaUrls
        self.caption = caption
        self.hashtags = hashtags
        self.postType = postType


    def __repr__(self):
        return str({"Text": self.text, "Media URLs" : self.mediaUrls})
    
    @abstractmethod
    def publishPost(self, publishingService):
        pass


