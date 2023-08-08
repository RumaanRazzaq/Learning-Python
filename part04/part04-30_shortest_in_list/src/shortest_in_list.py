# Write your solution here
def shortest(my_list):
    shortest_string = my_list[0]
    for i in my_list:
        if len(i) <= len(shortest_string):
            shortest_string = i
    return shortest_string