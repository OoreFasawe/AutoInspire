class Post:
    def __init__(self, imageUrl=None, text=None, fileName=""):
        # Each post should have a picture and some text
        self.fileName = fileName
        self.imageUrl = imageUrl
        self.text = text

    def __repr__(self):
        return str({"Text": self.text, "Image URL" : self.imageUrl})
