# Write your solution here
def everything_reversed(my_list):
    new_list = []
    for i in my_list:
        i = i[::-1]
        new_list.insert(0, i)
    return new_list