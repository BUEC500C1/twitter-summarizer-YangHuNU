import pytest
from main import main

prog_pass = 1

def test_sample1():
	try: 
		main("Yang199703")
	except(KeyError, NameError):
		assert prog_pass == 0
	else:
		assert prog_pass == 1

def test_sample2():


