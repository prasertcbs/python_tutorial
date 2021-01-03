from datetime import date, datetime

def retirement_date(dob:date):
    '''
    คำนวณวันเกษียณอายุราชการ
    ref: https://www.thairath.co.th/content/133598
    '''
    if (dob.month < 10) or (dob.month == 10 and dob.day == 1):
        return date(dob.year + 60, 9, 30)
    else:
        return date(dob.year + 61, 9, 30)

if __name__ == "__main__":
    # dob = date(1990, 5, 10)
    # dob = date(1990, 10, 2)
    # print(dob)
    # print(dob.year)
    # print(dob.month)
    # print(dob.day)
    dob_str = input('date of birth (yyyy-mm-dd): ')
    dob = datetime.strptime(dob_str, '%Y-%m-%d')
    print(f'dob = {dob}, retirement date = {retirement_date(dob)}')