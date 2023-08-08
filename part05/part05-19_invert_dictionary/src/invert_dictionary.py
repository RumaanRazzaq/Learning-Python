# Write your solution here
def invert(dictionary: dict):
    temp = {}
    for key, val in dictionary.items():
        temp[val] = key
    dictionary.clear()
    for key, val in temp.items():
        dictionary[key] = val