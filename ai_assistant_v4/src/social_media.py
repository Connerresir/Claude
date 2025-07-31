import tweepy
import os
import instaloader

class Twitter:
    def __init__(self):
        self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        self.consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        if not all([self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret]):
            print("Twitter API credentials not set. Please set the required environment variables.")
            self.client = None
        else:
            self.client = tweepy.Client(
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret
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

    def get_user_posts(self, username):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
            posts = []
            for post in profile.get_posts():
                posts.append({
                    "caption": post.caption,
                    "likes": post.likes,
                    "comments": post.comments,
                    "url": f"https://www.instagram.com/p/{post.shortcode}/"
                })
            return posts
        except Exception as e:
            return f"Error getting user posts: {e}"

    def send_dm(self, username, message):
        # This is a placeholder, as sending DMs is not well-supported by the Instagram API.
        print(f"Sending DM to {username}: {message}")
