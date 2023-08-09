# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    list = []
    for course in courses:
        if course["enabled"] == True:
            course_tuple = (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
            list.append(course_tuple)
    return list

def retrieve_course(course_name: str):
    address = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = address.read()
    course = json.loads(data)

    course_info = {}

    week_no = 0
    student = 0
    hours = 0
    exercise = 0
    
    for week, course_data in course.items():
        week_no += 1
        if student < int(course_data["students"]):
            student = course_data["students"]
        hours += course_data["hour_total"]
        exercise += course_data["exercise_total"]
    hours_average = hours // student
    exercise_average = exercise // student

    dict = {}
    dict["weeks"] = week_no
    dict["students"] = student
    dict["hours"] = hours
    dict["hours_average"] = hours_average
    dict["exercises"] = exercise
    dict["exercises_average"] = exercise_average
    return dict

if __name__ == "__main__":
    print(retrieve_all())
    print("\n\n\n\n")
    print(retrieve_course("docker2019"))