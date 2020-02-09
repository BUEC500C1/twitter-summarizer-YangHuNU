import os
import json
from google_vision_api import google_vision
from twitter_api import get_all_tweets

def main():
	print(get_all_tweets("Yang199703"))

if __name__ == '__main__':
	main()