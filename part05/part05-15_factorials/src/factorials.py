# Write your solution here
def factorials(n: int):
    new_dictionary = {}
    for i in range(1, n + 1):
        sum = 1
        count = 1
        while count <= i:
            sum *= count
            count += 1
        new_dictionary[i] = sum
        sum = 1
        count = 1
    return new_dictionary

if __name__ == "__main__":
    print(factorials(3))