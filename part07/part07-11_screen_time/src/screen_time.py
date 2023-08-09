# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
date = input("Starting date: ")
days_num = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

start_date = datetime.strptime(date, "%d.%m.%Y")
end_date = start_date + timedelta(days=days_num)
days = []
times = []
while start_date < end_date:
        day = start_date.strftime('%d.%m.%Y')
        days.append(day)
        screen_time = input(f'Screen time {day}: ')
        times.append(tuple(screen_time.split(' ')))
        start_date = start_date + timedelta(days=1)

print(f"Data stored in file {filename}")

with open(filename, "w") as file:
        file.write(f"Time period: {days[0]}-{days[days_num - 1]}\n")
        total_time = 0
        for time in times:
                total_time += int(time[0]) + int(time[1]) + int(time[2])
        file.write(f"Total minutes: {total_time}\n")
        file.write(f"Average minutes: {total_time / days_num}\n")
        for index, day in enumerate(days):
            file.write(f'{day}: {times[index][0]}/{times[index][1]}/{times[index][2]}\n')