# write your solution here

def read_file(filename):
    dict = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            words = line.split(";")
            if words[0] == "id":
                    continue
            dict[words[0]] = words[1:]
    return dict

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

student_dictionary = read_file(student_file)
exercise_dictionary = read_file(exercise_file)

for id, name in student_dictionary.items():
    exercise_sum = 0
    if id in exercise_dictionary:
        for exercise in exercise_dictionary[id]:
            exercise_sum += int(exercise)
    print(f"{name[0]} {name[1]} {exercise_sum}")
