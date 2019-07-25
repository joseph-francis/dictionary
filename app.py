import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))  # Converts to JSON to Python dictionary


def find(word):
    term = word.lower()

    if term in data:
        return data[term]
    elif len((get_close_matches(term, data.keys(), 1), 0.8)[0]) > 0:
        test_var = get_close_matches(term, data.keys(), 1, 0.8)[0]
        result = input("Did you mean %s? Enter Y if yes, N if no: " % test_var)
        if result == "Y":
            return data[test_var]

    return "The given word is not in my dictionary lol"


user_input = input("Enter the search term: ")
print(find(user_input))


# print(SequenceMatcher(None, "rainn", "rain").ratio())  # This will compare the similarity of these two words



