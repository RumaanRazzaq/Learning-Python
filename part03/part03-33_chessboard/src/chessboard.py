# Write your solution here
def chessboard(size):
    zero_or_one = 1
    width = 0
    height = 0
    while height < size:
        while width < size:
            if zero_or_one == 1:
                print("1", end="")
                zero_or_one = 0
            else:
                print("0", end="")
                zero_or_one = 1
            width += 1

        if size % 2 == 0 and height % 2 == 0:
            zero_or_one = 0
        elif size % 2 == 0:
            zero_or_one = 1

        height += 1
        width = 0
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(4)
