import sys
import os
sys.path.append(os.path.abspath('/Users/ooreoluwafasawe/Desktop/Coding/Instagram-Autobot'))
from Classes.Post import Post
from instabot.bot import Bot

class PostPublishingService:
    bot =  Bot()
    bot.login(username='butterman_32', password='ooreAutobot')
    # singleton design pattern in python
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostPublishingService, cls).__new__(cls)
        
        return cls.instance

    def publishPost(self, post:Post):
        #Calling upload here
        self.bot.upload_photo(post.imageUrl, caption= post.text)
        
        return

# demo functionality
if __name__ == "__main__":
    p = PostPublishingService()
    newPost = Post()
    newPost = p.publishPost()
    p.savePost(newPost)