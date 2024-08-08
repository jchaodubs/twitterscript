import tweepy
from config import API_KEY, API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET, BEARER_TOKEN, ACCOUNTS, KEYWORDS


auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class MyStreamingClient(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # see if the tweet is from one of the specified accounts
        if tweet.author.username in ACCOUNTS:
            # check if any of the keywords are in the tweet text
            if any(keyword in tweet.text for keyword in KEYWORDS):
                print(f"New tweet from {tweet.author.username} with keyword: {tweet.text}")
            else:
                print(f"Tweet from {tweet.author.username} does not contain any of the keywords.")
        else:
            print(f"Tweet from {tweet.author.username} is not from the specified accounts.")

    def on_error(self, status_code):
        if status_code == 420:
            return False

#something chatgpt????
streaming_client = MyStreamingClient(BEARER_TOKEN)
for account in ACCOUNTS:
    streaming_client.add_rules(tweepy.StreamRule(f"from:{account}"))

streaming_client.filter()
