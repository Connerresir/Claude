import tweepy
import os
import instaloader

# TODO: Set your Twitter API keys and access tokens as environment variables
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

class Twitter:
    def __init__(self):
        if not all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
            print("Twitter API credentials not set. Please set the required environment variables.")
            self.client = None
        else:
            self.client = tweepy.Client(
                consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token=ACCESS_TOKEN,
                access_token_secret=ACCESS_TOKEN_SECRET
            )

    def post_tweet(self, text):
        if not self.client:
            print("Twitter client not initialized.")
            return

        try:
            self.client.create_tweet(text=text)
            print(f"Tweeted: {text}")
        except Exception as e:
            print(f"Error posting tweet: {e}")

class Instagram:
    def __init__(self):
        self.L = instaloader.Instaloader()

    def get_user_info(self, username):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
            return {
                "username": profile.username,
                "followers": profile.followers,
                "followees": profile.followees,
                "posts": profile.mediacount,
                "biography": profile.biography,
            }
        except Exception as e:
            return f"Error getting user info: {e}"
