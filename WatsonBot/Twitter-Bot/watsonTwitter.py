#Twitter Bot for Watson
	#Machine Learning fun

import twitter
#imports my SECRET keys from keys.py. 
from keys import *
from pprint import pprint
import random 
from watsonsayings import * 

# Authenticate via OAuth
api = twitter.Api(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)


def postStatus(status, in_reply_tweet=None):
	""" Posts a Status, deleting any duplicate statuses.
    Parameters:
            status - Given status to post to twitter.

    Returns:
            results - The result of the PostUpdate call.
    """
	#Initialize flag, stringify status, and get a list of tweets from your account
	status = str(status)
	feed = api.GetUserTimeline("watsonthebetta")
	#For the tweet in the feed
	for tweet in feed:
		#If this tweet is a duplicate
		if status == tweet.text:
			#Destroy that tweet
			api.DestroyStatus(tweet.id)
	#Post the status and return the results
	return api.PostUpdate(status, in_reply_tweet)


def generateTweet(): 
	#Open activity.txt 
	filename = '/usr/share/nginx/www/watson/images/activity.txt'
	watson_activity = open(filename, 'r')
	#grab the first line and save it to activity 
	activity = watson_activity.readline() 
	#CLOSE THE DANG FILE 
	watson_activity.close()

	#You're a programming prodigy
	if activity == "hiding": 
		status = random.choice(hiding)
	else: 
		status = random.choice(swimming)

	postStatus(status + " http://www.gabbyortman.me/watson" + " #HackISU #BigBetta") 