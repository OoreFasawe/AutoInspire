from Post import Post, PostTypes
class VideoPost(Post):
    def __init__(self, fileName=None, mediaUrl=None, caption=None, hashtags=None):
        super.__init__(fileName, mediaUrl, caption, hashtags)
        self.numberOfPosts = 1
        self.postType = PostTypes.VIDEO
    
    def publishPost():
        pass