#!/usr/bin/env python
import tweepy #Installed on premises
import json
from google_vision_api import google_vision

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):

	#authentication
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#grabbing tweets
	alltweets = []
	new_tweets = api.user_timeline(screen_name = screen_name,count=1)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	while len(new_tweets) > 0:
		# print("getting tweets before %s" % oldest)
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1

		# print ("...%s tweets downloaded so far" % len(alltweets))

	#take the first 5 tweets with image and sent to google vision api for image interpretation
	counter = 5

	result = ''

	for tweet in alltweets:
		#not all tweets will have media url, so lets skip them
		try:
			print(tweet.entities['media'][0]['media_url'])
		except(NameError, KeyError):
			pass
		else:
			result += google_vision(tweet.entities['media'][0]['media_url'])
			result += '\n'
			counter = counter - 1
		if counter==0:
			break
	return result
				

if __name__ == '__main__':
	get_all_tweets("Yang199703")