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

def calculate_grade(exam_sum, exercise_sum):
    exercise_points = exercise_sum // 10
    total = exercise_points + exam_sum
    if total <= 14:
        return 0
    elif total <= 17:
        return 1
    elif total <= 20:
        return 2
    elif total <= 23:
        return 3
    elif total <= 27:
        return 4
    else:
        return 5
    
if True:
    student_file = input('Student information: ')
    exercise_file = input('Exercises completed: ')
    exam_points_file = input('Exam points: ')
else:
    student_file = 'students1.csv'
    exercise_file = 'exercises1.csv'        
    exam_points_file = 'exam_points1.csv'

student_dictionary = read_file(student_file)
exercise_dictionary = read_file(exercise_file)
exam_points_dictionary = read_file(exam_points_file)

for id, name in student_dictionary.items():
    exam_points_sum = 0
    if id in exam_points_dictionary:
        for exam_point in exam_points_dictionary[id]:
            exam_points_sum += int(exam_point)
    exercise_sum = 0
    if id in exercise_dictionary:
        for exercise in exercise_dictionary[id]:
            exercise_sum += int(exercise)
    exercise_sum = (exercise_sum / 40) * 100
    grade = calculate_grade(exam_points_sum, exercise_sum)
    print(f"{name[0]} {name[1]} {grade}")
