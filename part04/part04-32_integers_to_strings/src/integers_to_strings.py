# Write your solution here
def formatted(my_list):
    new_list = []
    for i in my_list:
        new_list.append(f"{i:.2f}")
    return new_list