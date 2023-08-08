# Write your solution here
def distinct_numbers(my_list):
    my_list = sorted(my_list)
    new_list = []
    for i in my_list:
        if not (i in new_list):
            new_list.append(i)
    return new_list