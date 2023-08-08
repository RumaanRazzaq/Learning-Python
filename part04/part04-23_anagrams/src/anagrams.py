# Write your solution here
def anagrams(word1, word2):
    sorted1 = sorted(word1)
    sorted2 = sorted(word2)
    if sorted1 == sorted2:
        return True
    else:
        return False