import unittest
import argparse

def unittests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test/', pattern='*_test.py')
    return test_suite

if __name__ == "__main__":
	main()