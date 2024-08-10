class Post:
    def __init__(self, img, text):
        self.image = img
        self.text = text

    def __repr__(self):
        return self.text
