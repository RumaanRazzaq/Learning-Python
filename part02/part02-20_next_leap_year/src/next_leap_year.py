# Write your solution here
year = int(input("Year: "))
temp_year = year
while True:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if year == temp_year:
            if (year+4) % 100 == 0:
                print(f"The next leap year after {temp_year} is {year + 8}")
            else:
                print(f"The next leap year after {temp_year} is {year + 4}")
        else: 
            print(f"The next leap year after {temp_year} is {year}")
        break
    else:
        year += 1