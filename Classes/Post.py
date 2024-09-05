from abc import abstractmethod
class Post:
    def __init__(self, fileName=None, mediaUrls=[], caption=None, hashtags=None):
        # Each post should have a picture and some text
        self.fileName = fileName
        self.mediaUrls = mediaUrls
        self.caption = caption
        self.hashtags = hashtags

    def __repr__(self):
        return str({"Text": self.text, "Media URLs" : self.mediaUrls})
    
    @abstractmethod
    def publishPost(self, publishingService):
        pass

from enum import Enum
class PostTypes(Enum):
    IMAGE = 1
    VIDEO = 2
    CAROUSEL = 3
