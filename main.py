import os
import json
from google_vision_api import google_vision
from twitter_api import get_all_tweets

def main(user):
	print(get_all_tweets(user))

if __name__ == '__main__':
	main("Yang199703")