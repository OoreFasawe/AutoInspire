from ..Classes import Post
class PostPublishingService:
    def __init__(self):
        self.postPublishingService = None
        pass

    def getPostPublishingService(self):
        # Singleton design
        if not self.postPublishingService:
            self.postPublishingService = PostPublishingService()
        
        return self.postPublishingService

    def publishPost(self):
        pass