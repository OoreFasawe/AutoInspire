from ..Classes import Post
class PostMakingService(object):
    def __new__(cls):
        # singleton design pattern in python
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostMakingService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        pass

    def savePost(self, post: Post):
        pass