import os
from openai import OpenAI 
from Classes.Post import Post
import firebase_admin
from firebase_admin import firestore, credentials, storage
import requests
import logging
import random
import replicate

logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=os.environ.get("LOG_LEVEL", "INFO"),
)

class PostCreationService(object):
    # Initialize openai, firebase database and firebase data storage clients.
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", 0))
    cred = credentials.Certificate(os.path.abspath('/Users/ooreoluwafasawe/Downloads/PersonalProjects/AutoInspire/Utility/firebaseServiceAccount.json'))
    firebase_admin.initialize_app(cred, {"storageBucket": "instagram-autobot-df35b.appspot.com"})
    db = firestore.client()
    bucket = storage.bucket()
    
    def __new__(cls):
        # Singleton design pattern in python.
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostCreationService, cls).__new__(cls)
        return cls.instance

    def createPost(self):
        logging.info("Starting Post Creation Service")
        if not os.environ.get("OPENAI_API_KEY"):
            logging.error("No OPENAI_API_KEY detected, please add one to your environment ")
            exit()
            
        previousPosts = self.retrieveList("./Cache/previousPosts.txt")
        newPost = Post()
        newPost.caption = self.generateCaption(previousPosts)
        newPost.hashtags = self.generateHashtags(newPost.caption)
        newPost.mediaUrl = self.generateImage(newPost.caption)
        newPost.fileName = self.createFileName()
        return newPost

    def savePost(self, post: Post):
        # save to firebase storage
        logging.info(f"Saving {post.fileName} to database...")
        blob = PostCreationService.bucket.blob(f"{post.fileName}.jpg")
        imageData = requests.get(post.mediaUrl).content
        blob.upload_from_string(
            imageData,
            content_type='image/jpg'
        )
        # change temporary url to firebase permanent url and store in database
        post.mediaUrl = blob.public_url
        blob.make_public()
        PostCreationService.db.collection("posts").add(document_id=post.fileName, document_data={"document" "text": post.caption, "hashtags": post.hashtags, "mediaUrl": post.mediaUrl})
        # update previous post cache 
        self.updateMostPreviousPosts(post.caption)
        logging.info(f"Saved {post.fileName} to database. Public url: {post.mediaUrl}\n")
        return
    
    def updateMostPreviousPosts(self, text):
        path = "./Cache/previousPosts.txt"
        with open(path, "r+") as f:
            f = open(path, "r+")
            _ = f.readline()
            data = f.read()
            f.seek(0)
            f.write(data)
            f.truncate()
            f.write(f"{text}\n")
        return

    def retrieveList(self, path):
        fileExists = os.path.isfile(path)
        if not fileExists:
            try:
                # create new file
                open(path, "x")
                with open(path, "a") as f:
                    for _ in range(20):
                        f.write("xx\n")
            except Exception as error:
                logging.error("file exists but for some reason was not found by system", error)

        # read file content
        with open(path, "r") as f:
            textList = []
            for _ in range(20):
                line = f.readline().rstrip("xx\n")
                if line:
                    textList.append(line)
        return textList
        
    def generateCaption(self, noRepeatList):
        logging.info("Generating caption...")
        motivationThemes = ["reward", "socialRecognition", "obligation", "fear", "socialStatus", "competition"]
        storyTypes = ["Linear Narrative", "Nonlinear Narrative", "Circular Narrative", "Framed Narrative", "Episodic Narrative", "Multi-Perspective Narrative", "Stream of Consciousness", "Epistolary Narrative", "Anthology Narrative", "Interactive Narrative", "Allegorical Narrative", "Metafiction", "Oral Tradition", "Found Footage Narrative", "Flashback Narrative"]
        randomTheme = random.choice(motivationThemes)
        logging.debug(f"Post Theme: {randomTheme}")
        prompts = self.retrieveList(f"./Utility/Prompts/{randomTheme}.txt")

        if not prompts:
            raise ValueError(f"Prompt list for theme '{randomTheme}' is empty. Check if the file exists and contains data.")
        
        randomPrompt = random.choice(prompts)
        logging.debug(f"Caption generation Prompt: {randomPrompt}")
        noRepeatListOnALine = " ".join(noRepeatList)
    
        textCompletion = PostCreationService.client.chat.completions.create(
            messages=[{"role": "user", "content": f"{randomPrompt}; no hashtags, just a text. If it is a story, follow the {random.choice(storyTypes)} storytelling type with specific scenarios ad interactions leading to speicifc results, shorter than 100 words.\
                       Also I just don't want it starting with a ' in a <someplace> where <some context>', be creative such that the variance of your results is high and creativity high\
                       This quote should follow a different pattern structure, probability of weirdness than from these quotes from previous posts:{noRepeatListOnALine}"}],
            model="gpt-4o-mini",
            temperature=0.8 
        ).to_dict()
        caption = textCompletion["choices"][0]["message"]["content"]
        logging.info(f"Caption: {caption}\n")
        return caption
    
    def generateHashtags(self, text):
        logging.info("Generating hashtags")
        hashtagCompletion = PostCreationService.client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": f"Make ten space-seperated relevant hashtags to this text on a single line):{text}."}],
        ).to_dict()
        hashtags = hashtagCompletion["choices"][0]["message"]["content"]
        logging.info(f"Hashtags: {hashtags}\n")
        return f"#Motivation {hashtags}"
    
    def generateImage(self, text):
        logging.info("Generating image...")
        # Define categories with possible values
        art_styles = ["photorealistic", "cinematic", "digital painting", "anime-inspired", "surrealist"]
        lighting_moods = ["warm golden hour", "moody and dramatic", "soft glow", "neon cyberpunk", "high contrast"]
        composition_styles = ["close-up portrait", "wide-angle shot", "dynamic perspective", "bird’s eye view", "symmetrical composition"]
        color_palettes = ["vibrant neon", "soft pastel", "earthy tones", "monochrome", "colorful gradients"]
        art_mediums = ["oil painting", "watercolor", "cyberpunk digital art", "sketch drawing", "charcoal illustration"]
        detail_levels = ["hyper-detailed", "minimalist", "abstract", "realistic with fine textures"]
        poses_emotions = ["powerful stance", "calm and serene", "determined expression", "energetic movement", "mysterious gaze"]

        imgGenerationPrePrompt = (
            f"Please generate an image generation prompt for the motivational caption '{text}'. Try not to be abstract with the description and the prompt should be structured in two parts: "
            "first, a 'Main Theme' that clearly describes the main idea, emotion, and message of the caption, making it the primary focus of the image; do not put any text at all on the image "
            "second, a 'Style Options' section that lists customizable artistic categories. "
            f"For the style options, feel free appeal to any combination of the following: lighting mood = {random.choice(lighting_moods)}, "
            f"composition = {random.choice(composition_styles)}, color palette = {random.choice(color_palettes)}, "
            f"art medium = {random.choice(art_mediums)}, detail level = {random.choice(detail_levels)}, "
            f"and pose/emotion = {random.choice(poses_emotions)}."
        )

        imageGenerationPrompt = PostCreationService.client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": imgGenerationPrePrompt}],
        ).to_dict()
        imgPrompt = imageGenerationPrompt["choices"][0]["message"]["content"]
        logging.debug(f"Image Generation prompt: \n{imgPrompt}\n")



        input = {
            "prompt": imgPrompt,
            "prompt_upsampling": True
        }

        output = replicate.run(
            "black-forest-labs/flux-1.1-pro",
            input=input
        )
        image_url = output[0] if isinstance(output, list) else output
        # print(image_url)
        # imageCompletion = PostCreationService.client.images.generate(
        #     model="dall-e-3",
        #     prompt=imgPrompt,
        #     size="1024x1024",
        #     style="vivid",
        # ).to_dict()
        mediaUrl = image_url #Completion["data"][0]["url"]
        logging.info(f"Image url: {mediaUrl}\n")
        return mediaUrl
    
    def createFileName(self):
        logging.info("Creating post file name...")
        postCollection = PostCreationService.db.collection("posts")
        # TODO(oore): Add count variable to database for faster lookup
        countQuery = postCollection.count()
        numberOfPosts = countQuery.get()[0][0].value
        fileName = f"Post#{int(numberOfPosts + 1)}"
        logging.info(f"File name: {fileName}\n")
        return fileName

# demo functionality
if __name__ == "__main__":
    p = PostCreationService()
    # previousPosts = p.retrieveList("./Cache/previousPosts.txt")
    p.createPost()
    # p.savePost(newPost)
