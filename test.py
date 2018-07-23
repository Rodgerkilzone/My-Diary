import unittest
import argparse

def unittests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test/', pattern='*_test.py')
    return test_suite
def main():
	parser = argparse.ArgumentParser(description = "tests for diary api")
	parser.add_argument("-unit", action="store_true", help="run unittests")
	args = parser.parse_args()

	runner = unittest.TextTestRunner(verbosity=1, buffer=True)


	if args.unit:
		runner.run(unittests())
		return

	parser.print_help()

if __name__ == "__main__":
	main()