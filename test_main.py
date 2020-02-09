import pytest
import tweepy
from main import test_run

prog_pass = 1

def test_sample1():
	try: 
		test_run('Yang199703')
	except(tweepy.TweepError):
		assert prog_pass == 1
	except(KeyError, NameError):
		assert prog_pass == 0
	else:
		assert prog_pass == 1

# def test_sample2():