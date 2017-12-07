#import json
from flask import Flask
from twitter import *


# Twitter API credentials
consumer_key = "bC1TasFS1FLvKMhvrDpzs0Ocb"
consumer_secret = "PknWLz7MqnLmz3zBYpZ55s4N6MOWKYzlI4XtKRWyjyY5v1Dg0e"
access_key = "938804144252391424-3QNUg9rnvLS2Ku60oJNssye8bXw98iI"
access_secret = "6f1BvYdj7fwesgUqIqqvn10ag9bVD8qJXrXZh1cq0eZZh"

app = Flask(__name__)

@app.route('/')
def get_all_tweets():
    print("hi")
    # authorize twitter, initialize tweepy
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_key, access_secret)
    #api = tweepy.API(auth)
    oauth = OAuth(access_key, access_secret, consumer_key, consumer_secret)

    # Initiate the connection to Twitter REST API
    twitter = Twitter(auth=oauth)

    # Search for latest tweets about "#CropBurning"
    query = twitter.search.tweets(q='#CropBurning')

    #-----------------------------------------------------------------------
    # Loop through each of the results, and print its content.
    #-----------------------------------------------------------------------
    for result in query['statuses']:
        return result['created_at']
        #print(result['user']['screen_name'])
        #print(result['text'])

#print json.dumps(tweet)