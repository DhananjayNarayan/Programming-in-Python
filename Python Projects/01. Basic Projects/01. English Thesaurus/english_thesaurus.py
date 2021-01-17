import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
    # if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters acronym words like USA
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Incorrect Word. Do you mean %s instead? Enter 'Y' for Yes, 'N' for No : " %
                   get_close_matches(word, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "The word doesn't exist. Please check or enter different a word."
        else:
            return "Incorrect Entry."
    else:
        return "The word doesn't exist. Please check or enter different a word."


word = input("Enter a Word: ")

output = (fetch(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
