from Utility.PostPublishingService import PostPublishingService
from Utility.PostCreationService import PostCreationService


if __name__ == "__main__":
    pCreate = PostCreationService()
    newPost = pCreate.createPost()
    pCreate.savePost(newPost)
    pPublish = PostPublishingService()
    pPublish.publishPost(newPost)