import pytest
from main import test_run1, test_run2, test_run3, test_run4

def test_sample1():
	try: 
		print(test_run1())
	except:
		assert 0
	else:
		assert 1

def test_sample2():
	try: 
		print(test_run2())
	except:
		assert 0
	else:
		assert 1

def test_sample3():
	try: 
 		print(test_run3())
	except:
		assert 0
	else:
		assert 1

def test_sample4():
	try: 
		print(test_run4())
	except:
		assert 0
	else:
		assert 1