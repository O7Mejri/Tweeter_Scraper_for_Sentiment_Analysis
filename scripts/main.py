import tweepy
import json
import os
from dotenv import load_dotenv

# relative path
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

# get the vars
load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

# Setup access to API v1
def connect_to_twitter_OAuthv1():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api
def connect_to_twitter_OAuthv2():
    auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
    api = tweepy.API(auth)
    return api
def connect_to_twitter_OAuthv3():
    auth = tweepy.OAuth2AppHandler(API_KEY, API_SECRET_KEY)
    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuthv2()


# Fetch user shit

tweets = []
username = 'mejri_DoRoyH'
count = 1
tweets = api.user_timeline(screen_name=username, count=count)

for tweet in tweets:
    print(tweet.text)
    
# Save raw tweet data to JSON file
with open('data/raw_data/tweets.json', 'w') as f:
    for tweet in tweets:
        json.dump(tweet._json, f)
        f.write('\n')
        
        
tweets = []
search_words = "#AIArt"
date_since = "2022-01-01"
# Get the tweets
try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since_id=date_since).items(20)
    # Pulling information from tweets iterable object
    for tweet in tweets:
        print(tweet.text)
except tweepy.TweepError as e:
    print("Error : " + str(e))
    
    
# tweets = []
# username = 'mejri_DoRoyH'
# count = 2
# # Get the tweets

# user = api.get_user(screen_name=username)
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

# try:
#     # Creation of query method using parameters
#     tweets = api.user_timeline(id=username, count=count)
#     # Pulling information from tweets iterable object
#     for tweet in tweets:
#         print(tweet.text)
# except tweepy.TweepError as e:
#     print("Error : " + str(e))
    
    
# # Define search criteria
# search_query = 'python'  # Example: scrape tweets related to Python programming
# language = 'en'  # Language filter (English)

# # Perform search query
# tweets = api.search(q=search_query, lang=language, count=100)  # Retrieve 100 tweets

