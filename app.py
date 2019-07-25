import json

data = json.load(open("data.json"))  # Converts to JSON to Python dictionary


def find(word):
    term = word.lower()
    if term in data:
        return data[term]

    return "The given word is not in my dictionary lol"


user_input = input("Enter the search term: ")
print(find(user_input))


