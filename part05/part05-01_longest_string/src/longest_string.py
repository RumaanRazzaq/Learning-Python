# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for i in strings:
        if len(longest) < len(i):
            longest = i
    return longest