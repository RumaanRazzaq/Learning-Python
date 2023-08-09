# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):

    try:
        day = int(pic[0] + pic[1])
        month = int(pic[2] + pic[3])
        year = ""
        if pic[6] == "+":
            year = int("18" + pic[4] + pic[5])
        elif pic[6] == "-":
            year = int("19" + pic[4] + pic[5])
        elif pic[6] == "A":
            year = int("20" + pic[4] + pic[5])

        z = pic[10]
        nums = pic[0:6] + pic[7:10]
        index = int(nums)%31
        control = '0123456789ABCDEFHJKLMNPRSTUVWXY'[index]

        if day < 1 or day > 31 or month < 1 or month > 12 or pic[6] not in ('-','+','A') or z != control or len(pic) != 11:
                return False
    
        dob = datetime(year, month, day)
        
        return True
    
    except:
        return False
    
if __name__ == "__main__":
    print(is_it_valid("081842-720N"))
    print(is_it_valid("310286+713J"))
    print(is_it_valid("290200-1239"))