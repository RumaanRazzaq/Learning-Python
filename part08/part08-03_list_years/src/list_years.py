# Write your solution here
# Remember the import statement
from datetime import datetime

def list_years(dates: list):
    list = []
    for date in dates:
        list.append(date.year)
    list.sort()
    return list