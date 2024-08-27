class Post:
    def __init__(self, mediaUrl=None, text=None, fileName=""):
        # Each post should have a picture and some text
        self.fileName = fileName
        self.mediaUrl = mediaUrl
        self.text = text

    def __repr__(self):
        return str({"Text": self.text, "Media URL" : self.mediaUrl})
