# Write your solution here
def length_of_longest(my_list):
    length = 0
    for i in my_list:
        if len(i) > length:
            length = len(i)
    return length