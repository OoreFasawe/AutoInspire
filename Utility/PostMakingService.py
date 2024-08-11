from ..Classes import Post
class PostMakingService:
    def __init__(self):
        self.postMakingService = None
        pass

    def getPostMakingService(self):
        # Singleton design
        if not self.postMakingService:
            self.postMakingService = PostMakingService()
        
        return self.postMakingService

    def createPost(self):
        pass

    def savePost(self, post: Post):
        pass