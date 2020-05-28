# come up w/ a function that gets as input the key
# and returns a value for that particular key
# incorporate loading of the json file
# print the output
import json
import difflib


def main():
    dict_data = json.load(open('data.json'))
    word = input('Enter word: ')
    word = validate(word.lower(), dict_data)
    if word is False:
        return
    translate(word, dict_data)


def validate(key, data):
    if key in data:
        return key
    elif len(difflib.get_close_matches(key, data)) > 0:
        while True:
            alt_word = difflib.get_close_matches(key, data.keys(), n=1)[0]
            print('Did you mean {} instead? '.format(alt_word))
            action = input('Enter Y if yes, or N if no: ')
            if action == 'Y':
                word = difflib.get_close_matches(key, data.keys(), n=1)[0]
                return word
            elif action == 'N':
                print('The word doesn\'t exist. Please double check it.')
                return False
            else:
                print('Try again. Y or N')
    else:
        print('The word doesn\'t exist. Please double check it.')
        return False


def translate(key, data):
    print('\n'.join("{}".format(info) for info in data.get(key)))
    return


if __name__ == '__main__':
    main()
