import pytest
import tweepy
from main import test_run

prog_pass = 1

def test_sample1():
	try: 
		print(test_run())
	except(tweepy.TweepError):
		assert 1
	except(KeyError, NameError):
		assert 0
	else:
		assert 1

# def test_sample2():