from datetime import date

# pip install python-dateutil
from dateutil.relativedelta import relativedelta

def how_old_ymd(dob):
    age = relativedelta(date.today(), dob)
    print(age)
    return age.years, age.months, age.days


print(date.today())
# print(how_old_ymd(date(1997, 7, 10)))
y, m, d = how_old_ymd(date(1997, 7, 10))
print("{} year {} month {} days".format(y, m, d))
