# AutoInspire  
Instagram Account: [butterman_411](https://www.instagram.com/butterman_411/)  
<img src="https://firebasestorage.googleapis.com/v0/b/instagram-autobot-df35b.appspot.com/o/InstagramAccountScreenshot.jpg?alt=media&token=71a7405b-e15a-4dba-ad2e-472e256bd9de" alt="Screenshot of instagram page" width="370" height="700">

<img src="https://firebasestorage.googleapis.com/v0/b/instagram-autobot-df35b.appspot.com/o/Sample%20IG%20Post.jpeg?alt=media&token=5976a43e-5fc0-4a11-aa67-b7ac00716e14" alt="Screenshot of sample ig post" width="370" height="600">

## Purpose  
AutoInspire is a project built to generate and publish motivational posts on Instagram. While designed for motivational content, the framework is flexible enough to support any theme for creating an Instagram account via using differrent prompts.

## Overview  
The project is divided into two primary services: the post creation service, which uses OpenAI's ChatGPT and DALL-E models to generate captions, hashtags and images, and the post publishing service, which handles interactions with the Instagram account via the Facebook and Instagram Graph APIs. All post data is stored in Google Firebase database and storage. Additional services may be introduced as the project evolves and more features are added.

## Setup  
Coming soon...

## Development notes 
This project is still in development, and while the design isn't final, I’ve prioritized delivering a functional version first. Some aspects, such as file path management, absence of a dedicated logger for different logging priorities, and processes that could be run asynchronously, are still rough and will be refined over time. Since this is a personal project, it’s currently tailored to my own needs, but adjustments could be made later if it’s extended for broader use. My focus for now is tackling the most challenging and urgent requirements before refining other aspects.