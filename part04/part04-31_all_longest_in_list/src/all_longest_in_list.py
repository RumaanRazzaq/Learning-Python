# Write your solution here
def all_the_longest(my_list):
    length = 0
    for i in my_list:
        if len(i) > length:
            length = len(i)

    new_list = []
    for i in my_list:
        if len(i) == length:
            new_list.append(i)
    return new_list