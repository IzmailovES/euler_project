#!/usr/bin/env python3

class the_day:
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    def __init__(self, day, month, year, week):
        self.day = day
        self.month = month
        self.year = year
        self.week = week
    
    def __next_week(self):
        self.week = (1) if (self.week == 7) else (self.week + 1)

    def __next_month(self):
        self.month =  (1) if (self.month == 12) else (self.month + 1)
        return self.month == 1

    def next_day(self):
        self.__next_week()
        days_count = the_day.months[self.month]
        if (self.month == 2) and (not(self.year%4)) and (self.year%100):
            days_count += 1
        self.day += 1
        if self.day == (days_count + 1):
            self.day = 1
            if self.__next_month():
                self.year += 1
    def __str__(self):
        return f'today {self.day}.{self.month}.{self.year}, {self.week}'


day = the_day(1,1,1900,1)
print(day)
while day.year != 1901:
    #while not(day.year == 2023 and day.month == 10 and day.day == 30):
    day.next_day()
print(day)
acc = 0
while not((day.year == 2001)):
    if day.week == 7 and day.day == 1:
        acc += 1
    day.next_day()
print(day ,  'sundays:', acc)
        


