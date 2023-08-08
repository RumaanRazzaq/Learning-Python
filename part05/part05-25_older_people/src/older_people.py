# Write your solution here
def older_people(people: list, year: int):

    new_list = []

    for i in people:
        if i[1] < year:
            new_list.append(i[0])

    return new_list

