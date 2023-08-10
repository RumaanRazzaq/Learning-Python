# Write your solution here:
class Clock:
    def __init__(self, hour, min, second):
        self.seconds = second
        self.minutes = min
        self.hours = hour

    def set(self, hour, min):
        self.hours = hour
        self.minutes = min
        self.seconds = 0

    def tick(self):
        if self.hours == 23 and self.seconds == 59 and self.minutes == 59:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        elif self.seconds == 59 and self.minutes == 59 and self.hours != 23:
            self.seconds = 0
            self.minutes = 0
            self.hours += 1
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1
    
    def __str__(self) -> str:
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

if __name__ == "__main__":
    watch = Clock()
    for i in range(86400):
        print(watch)
        watch.tick()
