import pytest
from google_vision_api import google_vision
from twitter_api import get_all_tweets

def test_run1():
	"""My twitter less than 5 pictures were uploaded"""
	return get_all_tweets("Yang199703")

def test_run2():
	return get_all_tweets("ShawnMendes")

def test_run3():
	return get_all_tweets("MeetAnimals")

def test_run4():
	return get_all_tweets("")

if __name__ == '__main__':
	print("----------Data from test_run1----------")
	print(test_run1())
	print("----------Data from test_run2----------")
	print(test_run2())
	print("----------Data from test_run3----------")
	print(test_run3())
	print("----------Data from test_run4----------")
	print(test_run4())