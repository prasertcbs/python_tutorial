import calendar
from datetime import date, datetime


def children_day(year):
    i = 1
    while True:
        d = date(year, 1, i)
        if d.weekday() == calendar.SATURDAY:  # MON = 0, SUN = 6
            return date(year, 1, i + 7)
        else:
            i += 1

def thanksgiving_day(year):
    i = 1
    while True:
        d = date(year, 11, i)
        if d.weekday() == calendar.THURSDAY:  # MON = 0, SUN = 6
            return date(year, 11, i + 21)
        else:
            i += 1

year = 2016
# print(children_day(year))
calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.month(year, 1))

t = thanksgiving_day(year)
print(datetime.strftime(t, "%A %d-%B-%Y"))
print(calendar.month(year, 11))
