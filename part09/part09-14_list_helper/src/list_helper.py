# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest = my_list[0]
        greatest_count = 1
        for number in my_list:
            if my_list.count(number) > greatest_count:
                greatest_count = my_list.count(number)
                greatest = number
        return greatest

    @classmethod
    def doubles(cls, my_list: list):
        new_list = []
        unique_list = []
        for number in my_list:
            if number not in unique_list:
                unique_list.append(number)
            new_list.append(number)
        i = 0
        for number in unique_list:
            new_list.remove(number)
            try:
                new_list.remove(number)
                i += 1
            except:
                pass
        return i