
import tweepy
import json
import random

import os
from dotenv import load_dotenv


# Access the environment variables
load_dotenv('../.env')

client = tweepy.Client(consumer_key=os.getenv('CONSUMER_KEY'),
                       consumer_secret=os.getenv('CONSUMER_SECRET'),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_SECRET"))


# Authenticate with Twitter API
auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_SECRET"))


# Create API client
api = tweepy.API(auth)


# Load lyrics from JSON file
with open('lana_del_ray_lyrics.json') as file:
    data = json.load(file)

# Select a random song from the JSON data
song = random.choice(data['songs'])
title = song['title']
lyrics = song['lyrics']

# Format the lyrics as a tweet
tweet = f"🎵 {title} 🎵\n\n{lyrics}"

# Post the tweet
api.update_status(tweet)

# Print a message if the tweet was posted successfully
if api.last_response.status_code == 200:
    print("Tweet posted successfully!")
else:
    print("Error posting tweet:", api.last_response.status_code)