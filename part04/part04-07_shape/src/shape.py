# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

def shape(width, char, height, filler):
    i = 0
    while i <= width:
        line(i, char)
        i += 1 

    i = 0
    while i < height:
        line(width, filler)
        i += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")