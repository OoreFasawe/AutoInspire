from openai import OpenAI 
from ..Classes import Post
class PostCreationService(object):
    def __new__(cls):
        # singleton design pattern in python
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostCreationService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        client = OpenAI()

    def savePost(self, post: Post):
        pass