import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
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

print(fetch(word))
