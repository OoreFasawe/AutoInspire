import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes import Post
class PostPublishingService:
    # singleton design pattern in python
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
        return cls.instance

    def publishPost(self, post:Post):
        pass