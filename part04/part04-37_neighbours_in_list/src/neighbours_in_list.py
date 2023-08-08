# Write your solution here
def longest_series_of_neighbours(my_list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

if __name__ == "__main__":
    print(longest_series_of_neighbours([5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]))