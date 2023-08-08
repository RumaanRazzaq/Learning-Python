# Write your solution here
def no_vowels(my_string):
    for i in my_string:
        if i == "a":
            my_string = my_string.replace(i, "")
        elif i == "e":
            my_string = my_string.replace(i, "")
        elif i == "i":
            my_string = my_string.replace(i, "")
        elif i == "o":
            my_string = my_string.replace(i, "")
        elif i == "u":
            my_string = my_string.replace(i, "")
    return my_string