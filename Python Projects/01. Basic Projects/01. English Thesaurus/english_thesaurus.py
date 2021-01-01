import json

data = json.load(open("data.json"))


def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please check and enter different a word."


word = input("Enter a Word: ")

print(fetch(word))
