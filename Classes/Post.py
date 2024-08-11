class Post:
    def __init__(self, img, text):
        # each post should have a picture and some text
        self.image = img
        self.text = text

    def __repr__(self):
        return self.text
