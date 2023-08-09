# write your solution here

def largest():
    largest = 0
    with open("src/numbers.txt") as new_file:
        for line in new_file:
            if int(line) > largest:
                largest = int(line)
    return largest 

if __name__ == "__main__":
    print(str(largest()))