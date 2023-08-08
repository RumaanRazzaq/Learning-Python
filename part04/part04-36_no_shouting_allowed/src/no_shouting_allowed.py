# Write your solution here
def no_shouting(my_list):
    new_list = []
    for i in my_list:
        if not (i.isupper()):
            new_list.append(i)
    return new_list