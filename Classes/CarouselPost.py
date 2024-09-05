from Post import Post, PostTypes
class CarouselPost(Post):
    def __init__(self, fileName=None, mediaUrl=None, caption=None, hashtags=None):
        super.__init__(fileName, mediaUrl, caption, hashtags)
        self.numberOfPosts = 5
        self.postType = PostTypes.CAROUSEL