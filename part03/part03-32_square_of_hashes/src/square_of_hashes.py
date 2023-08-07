# Write your solution here
def hash_square(length):
    width = 0
    height = 0
    while height < length:
        while width < length:
            print("#", end="")
            width += 1
        height += 1
        width = 0
        print()


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)