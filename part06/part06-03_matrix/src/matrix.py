# write your solution here
def matrix_sum():
    total = 0
    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for number in numbers:
                total += int(number)
    return total

def matrix_max():
    greatest = 0
    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            if int(max(numbers)) > greatest:
                greatest = int(max(numbers))
    return greatest

def row_sums():
    sums = []
    with open("src/matrix.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            total = 0
            for number in numbers:
                total += int(number)
            sums.append(total)
    return sums

if __name__ == "__main__":
    print(row_sums())
    print(matrix_max())
    print(matrix_sum())