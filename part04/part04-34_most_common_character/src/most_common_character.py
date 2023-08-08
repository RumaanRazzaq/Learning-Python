# Write your solution here
def most_common_character(string1):
    most = string1[0]
    for i in string1:
        if string1.count(i) > string1.count(most):
            most = i
    return most