# Write your solution here
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

def space(num):
    print(" " * num, end="")

def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        space(size - i)
        line((i * 2) - 1, "*")
        i += 1
    space(size - 1)
    print("*")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)