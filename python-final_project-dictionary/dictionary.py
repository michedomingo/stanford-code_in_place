# come up w/ a function that gets as input the key 
# and returns a value for that particular key
# incorporate loading of the json file
# print the output
import json


def main():
	dict_data = json.load(open('data.json'))
	word = input('Enter word: ')
	word = validate(word.lower(), dict_data)
	translate(word, dict_data)

def validate(key, data):
	if key in data.keys():
		return key

def translate(key, data):
	print('\n'.join("{}".format(info) for info in data.get(key)))
	return

if __name__ == '__main__':
	main()
