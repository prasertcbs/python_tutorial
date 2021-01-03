import datetime
import calendar as cal

def friday13(year):
    # month_with_friday13 = []
    # for i in range(1, 13):
    #     d = datetime.date(year, i, 13)
    #     if d.weekday() == cal.FRIDAY:
    #         month_with_friday13.append(i)
    # return month_with_friday13
    return [i for i in range(1, 13) if datetime.date(year, i, 13).weekday() == cal.FRIDAY]

year = 2018
print(friday13(year))
m = friday13(year)
cal.setfirstweekday(cal.SUNDAY)
for i in m:
    print(cal.month(year, i))
