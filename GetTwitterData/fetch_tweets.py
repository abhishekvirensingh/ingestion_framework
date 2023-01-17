import tweepy
import configparser

# Get keys using config file

config = configparser.ConfigParser()
config.read('config.ini')

try:
    api_key = config['twitter_keys']['api_key']
    api_key_secret = config['twitter_keys']['api_secret_key']
    bearer_token = config['twitter_keys']['bearer_token']

except:
    print("There is an issue in getting the values from config.ini file")

# client creation and query:

client = tweepy.Client(bearer_token=bearer_token)

query = 'covid has:geo'
tweet_fields = ['created_at', 'lang']
expansions = ['author_id', 'geo.place_id']

try:
    response = client.search_recent_tweets(
        query=query, max_results=10, tweet_fields=tweet_fields,
        expansions=expansions)
except:
    raise ConnectionRefusedError("Netwrok not connected !")

for tweet in response.data:
    print(tweet)
