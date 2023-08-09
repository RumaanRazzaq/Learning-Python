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

def calculate_grade(total):
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

words = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{words[0]:30}{words[1]:10}{words[2]:10}{words[3]:10}{words[4]:10}{words[5]:10}")
for id, name in student_dictionary.items():
    exam_points_sum = 0
    if id in exam_points_dictionary:
        for exam_point in exam_points_dictionary[id]:
            exam_points_sum += int(exam_point)
    exercise_sum = 0
    if id in exercise_dictionary:
        for exercise in exercise_dictionary[id]:
            exercise_sum += int(exercise)
    exercise_sum2 = (exercise_sum / 40) * 100
    exercise_points = int(exercise_sum2 // 10)
    total = exercise_points + exam_points_sum
    grade = calculate_grade(total)
    name = name[0] + " " + name[1]
    print(f"{name:30}{exercise_sum:<10}{exercise_points:<10}{exam_points_sum:<10}{total:<10}{grade:<10}")
