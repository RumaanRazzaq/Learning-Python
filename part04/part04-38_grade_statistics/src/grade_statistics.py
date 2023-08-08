# Write your solution here

sum = 0
count = 0
grade_list = [0, 0, 0, 0, 0, 0]

while True:
    exam_input = input("Exam points and exercises completed: ")
    split_results = exam_input.split(" ")
    if exam_input == "":
        break
    points = int(split_results[1]) // 10 + int(split_results[0])

    sum += points
    count += 1

    if int(split_results[0]) < 10:
        grade_list[0] = grade_list[0] + 1
        continue
    
    if points <= 14:
        grade_list[0] = grade_list[0] + 1
    elif 15 <= points <= 17:
        grade_list[1] = grade_list[1] + 1
    elif 18 <= points <= 20:
        grade_list[2] = grade_list[2] + 1
    elif 21 <= points <= 23:
        grade_list[3] = grade_list[3] + 1
    elif 24 <= points <= 27:
        grade_list[4] = grade_list[4] + 1
    elif 28 <= points <= 30:
        grade_list[5] = grade_list[5] + 1

sum_of_grades = grade_list[0] + grade_list[1] + grade_list[2] + grade_list[3] + grade_list[4] + grade_list[5]

percentage = ((sum_of_grades - grade_list[0]) / sum_of_grades) * 100

print("Statistics:")
print(f"Points average: {sum / count}")
print(f"Pass percentage: {percentage:.1f}")
print("Grade distribution:")
print("  5: " + "*" * grade_list[5])
print("  4: " + "*" * grade_list[4])
print("  3: " + "*" * grade_list[3])
print("  2: " + "*" * grade_list[2])
print("  1: " + "*" * grade_list[1])
print("  0: " + "*" * grade_list[0])