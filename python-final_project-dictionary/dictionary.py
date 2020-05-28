# come up w/ a function that gets as input the key 
# and returns a value for that particular key
# incorporate loading of the json file
# print the output
import json


def main():
	data = json.load(open('data.json'))
	print(data)

	# validate(word.lower())





if __name__ == '__main__':
	main()
