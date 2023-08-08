# Write your solution here
def even_numbers(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

if __name__  == "__main__":
    print(even_numbers([1, 2, 3, 4, 5, 6]))