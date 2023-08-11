# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [word for word in words if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u"]