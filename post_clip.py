import json
import praw
import random
from dotenv import load_dotenv
import os

load_dotenv()

token = ""




client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
user_agent = "Strimis10"
redirect_uri = "http://localhost:8080"
refresh_token = os.getenv("refresh_token")


def post_todays_clip():
    with open("clips.json") as f:
        feeds = json.load(f)

    if feeds != []:
        todays_clip = random.choice(feeds)

        subr = 'lightswith'
        

        reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent,
                            redirect_uri=redirect_uri,
                            refresh_token=refresh_token)

        subreddit = reddit.subreddit(subr)

        title = "Today's Clip (test)"



        subreddit.submit(title,url=todays_clip)

        feeds.remove(todays_clip)

        with open("clips.json", mode='w') as f:
            f.write(json.dumps(feeds, indent=2)) 

