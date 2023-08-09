# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

dob = datetime(year, month, day)
milenium = datetime(1999, 12, 31)
difference = milenium - dob

if dob > milenium:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.")