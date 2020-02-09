import os
import json
from google_vision_api import google_vision
from twitter_api import get_all_tweets

def test_run(string_name):
	print(get_all_tweets(string_name))

if __name__ == '__main__':
	test_run("Yang199703")