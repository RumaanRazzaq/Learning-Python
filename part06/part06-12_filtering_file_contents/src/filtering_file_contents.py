# Write your solution here
def read_file():
    list  = []
    count = 0
    with open("solutions.csv") as file:
        for line in file:
            count += 1
            line = line.replace("\n", "")
            words = line.split(";")
            list.append((words[0], words[1], words[2]))
    print(len(list))
    return list

def filter_solutions():
    solutions = read_file()
    open("correct.csv", "w").close()
    open("incorrect.csv", "w").close
    for solution in solutions:
        question = solution[2]
        problem = solution[1]
        val = 0
        if "+" in problem:
            numbers = problem.split("+")
            val = int(numbers[0]) + int(numbers[1])
        else:
            numbers = problem.split("-")
            val = int(numbers[0]) - int(numbers[1])
        text_to_add  = f"{solution[0]};{solution[1]};{solution[2]}"
        if int(val) == int(question):
            with open("correct.csv", "a") as file:
                file.write(text_to_add + "\n")
        else:
            with open("incorrect.csv", "a") as file:
                file.write(text_to_add + "\n")

if __name__ == "__main__":
    filter_solutions()