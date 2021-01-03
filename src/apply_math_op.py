# print(2016 % 4)
# print(2559 % 4)

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def leap_year_buddhist(year):
    if year % 4 == 3:
        return True
    else:
        return False

def is_even(n):
    return True if n % 2 == 0 else False
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

def is_odd(n):
    return not(is_even(n))
    # if n % 2 == 1:
    #     return True
    # else:
    #     return False

def promotion(come, pay, per_head, pax):
    # come 4, pay 2
    # come 5, pay = ?
    # per_head = 100
    # 200 + 100
    return (pax // come) * (pay * per_head) + (pax % come) * per_head

# print(leap_year(2015))
# print(leap_year_buddhist(2559))
# print(is_even(5))
# print(is_odd(5))
print(promotion(4, 2, 100, 4))