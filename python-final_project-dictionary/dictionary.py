# come up w/ a function that gets as input the key
# and returns a value for that particular key
# incorporate loading of the json file
# print the output
import json
import difflib


def main():
    dict_data = json.load(open('data.json'))
    while True:
        word = input('\nEnter word: ')
        word = update_case(word, dict_data)
        word = validate(word, dict_data)
        if word is False:
            pass
        else:
            translate(word, dict_data)


def update_case(key, data):
    if key.lower() in data:
        key = key.lower()
        return key
    elif key.capitalize() in data:
        key = key.capitalize()
        return key
    elif key.upper() in data:
        key = key.upper()
        return key    
    else:
        return key


def validate(key, data):
    if key in data:
        return key
    elif len(difflib.get_close_matches(key, data)) > 0:
        while True:
            alt_word = difflib.get_close_matches(key, data.keys(), n=1)[0]
            print('\nDid you mean {} instead? '.format(alt_word))
            action = input('Enter Y if yes, or N if no: ')
            if action == 'Y':
                word = difflib.get_close_matches(key, data.keys(), n=1)[0]
                return word
            elif action == 'N':
                print('\n\tHmmm...no results found for {}. Please spell check and try again. 🤓'.format(key))
                return False
            else:
                print('\n\tTry again. Y or N')
    else:
        print('\n\tHmmm...no results found for {}. Please spell check and try again. 🤓'.format(key))
        return False


def translate(key, data):
    print('\n'.join("\n\t{}".format(info) for info in data.get(key)))
    return


if __name__ == '__main__':
    main()
