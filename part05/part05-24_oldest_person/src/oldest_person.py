# Write your solution here
def oldest_person(people: list):
    oldestName = people[0][0]
    oldestAge = people[0][1]
    
    for i in people:
        if i[1] < oldestAge:
            oldestAge = i[1]
            oldestName = i[0]

    #print(oldestAge)
    return (oldestName)  