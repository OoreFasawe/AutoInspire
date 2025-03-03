# from Utility.PostPublishingService import PostPublishingService
from Utility.PostCreationService import PostCreationService
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting AutoSpire")
    pCreate = PostCreationService()
    newPost = pCreate.createPost()
    pCreate.savePost(newPost)
    # pPublish = PostPublishingService()
    # pPublish.publishPost(newPost)