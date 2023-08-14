# Write your solution here
def add_student(student_dict, name):
    student_dict[name] = []

def print_student(student_dict, name):
    for student, courses in student_dict.items():
        if student == name:
            print(name + ":")
            if len(courses) == 0:
                print(" no completed courses")
                return
            else:
                print(f" {len(courses)} completed courses:")
                grade_sum = 0
                for course in courses:
                    print("  " + course[0], course[1])
                    grade_sum += course[1]
                print(f" average grade {grade_sum / len(courses)}")
                return
    print(name + ": no such person in the database")    

def add_course(database: dict, student: str, course: tuple):
    test = []
    list_tuple = []

    if database[student] == "no completed courses" or database[student] == "": 
        database[student] = []

    database[student].append(tuple(course))
    copy = sorted(database[student])[::-1]

    for key, value in database.items():
        if value == "":
            continue
    
    for subject, grade in copy:
        if subject not in test and grade > 0:
            test.append(subject) 
            test.append(grade) 
    
    for i in range(len(test) - 1):  
        pair = test[i], test[i + 1] 
        if pair not in list_tuple and i % 2 == 0: 
            list_tuple.append(pair)
    
    database[student] = list_tuple

def summary(student_dict):
    print(f"students {len(student_dict)}")
    name_most = ""
    most_courses = 0
    name_average = ""
    average_grade = 0
    for student, courses, in student_dict.items():
        if len(courses) > most_courses:
            name_most = student
            most_courses = len(courses)
        temp_average = 0
        for course in courses:
            temp_average += course[1]
        if average_grade < temp_average / len(courses):
            average_grade = temp_average / len(courses)
            name_average = student
    print(f"most courses completed {most_courses} {name_most}")
    print(f"best average grade {average_grade} {name_average}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)