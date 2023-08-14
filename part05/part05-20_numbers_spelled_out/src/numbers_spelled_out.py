# Write your solution here
def dict_of_numbers():
    dict = {}
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    for i in range(0, 100):
        dict[0] = "zero"  
        if i >= 1 and i <= 9:  
            dict[i] = ones[i]
        elif i >= 10 and i <= 19:  
            dict[i] = teens[i - 10] 
        elif i % 10 == 0:
            dict[i] = tens[i // 10]
        else:  
            dict[i] = tens[i // 10] + "-" + ones[i % 10]
    return dict

if __name__ == "__main__":
    nums = dict_of_numbers()
    print(nums[0])