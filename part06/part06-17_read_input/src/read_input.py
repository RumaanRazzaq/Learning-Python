# Write your solution here
def read_input(string, x, y):
    while True:
        try:
            num = int(input(string))
        except:
            num = 555
        if x < num < y:
            print("You typed in:", num)
            return num
        else:
            print(f"You must type in an integer between {x} and {y}")