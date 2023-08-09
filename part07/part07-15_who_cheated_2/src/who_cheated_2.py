# Write your solution here
import csv
from datetime import datetime, timedelta

def get_students_exam_data() -> dict:
    students = {}
    with open('start_times.csv') as start_file:
        for line in csv.reader(start_file, delimiter=';'):
            student = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students[student] = {
                'start_time' : start_time,
                #'start_time' : line[1],
                'stats' : {
                    'tasks' : [],
                    'points' : [],
                    'submission_times' : []
                }
            }

    with open('submissions.csv') as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            student = line[0]
            task = int(line[1])
            point = int(line[2])
            sub_time = datetime.strptime(line[3], '%H:%M')
            students[student]['stats']['tasks'].append(task)
            students[student]['stats']['points'].append(point)
            students[student]['stats']['submission_times'].append(sub_time)
    
    return students

def cheaters():
    data = get_students_exam_data()
    cheaters = []
    for student, info in data.items():
        start_time = info['start_time']
        submission_times = info['stats']['submission_times']
        for time in submission_times:
            if time > (start_time + timedelta(hours=3)):
                cheaters.append(student)
                break
            
    return cheaters

def final_points():
    final_points = {}
    data = get_students_exam_data()
    for student, info in data.items():
        total_points = 0
        start_time = info['start_time']
        tasks = info['stats']['tasks']
        for task in range(1, 9):
            indices = [i for i, v in enumerate(tasks) if v == task]
            max_point = 0
            for index in indices:
                point = info['stats']['points'][index]
                sub_time = info['stats']['submission_times'][index]
                if sub_time <= (start_time + timedelta(hours=3)):
                    if point > max_point:
                        max_point = point
            total_points += max_point
        final_points[student] = total_points
    return final_points

if __name__ == "__main__":
    print(cheaters())