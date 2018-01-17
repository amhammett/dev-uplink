import argparse
import os


def validate_path(path):
	return os.path.exists(path)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', default='~')
	return parser.parse_args()


def main():
	args = parse_args()
	if(validate_path(args.path)):
		print(args)
	else:
		print('invalid path provided')


if __name__ == '__main__':
	main()