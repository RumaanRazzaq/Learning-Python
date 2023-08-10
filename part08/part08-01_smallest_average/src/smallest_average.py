# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    person1_total = int(person1["result1"]) + int(person1["result2"]) + int(person1["result3"])
    person1_average = person1_total / 3
    person2_total = int(person2["result1"]) + int(person2["result2"]) + int(person2["result3"])
    person2_average = person2_total / 3
    person3_total = int(person3["result1"]) + int(person3["result2"]) + int(person3["result3"])
    person3_average = person3_total / 3
    if person1_average < person2_average and person1_average < person3_average:
        return person1
    elif person2_average < person1_average and person2_average < person3_average:
        return person2
    else:
        return person3