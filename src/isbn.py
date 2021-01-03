# https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation
from itertools import cycle


def isbn_checkdigit(isbn):
    total = 0
    for m, c in zip((1,3) * 6, isbn[:12]):
        total += m * int(c)
        # print(m, int(c))
    x = total % 10
    return 0 if x == 0 else 10 - x

def isbn_checkdigit2(isbn):
    total = 0
    for m, c in zip(cycle((1,3)), isbn[:12]):
        total += m * int(c)
        # print(m, int(c))
    x = total % 10
    return 0 if x == 0 else 10 - x

def isbn_checkdigit3(isbn):
    x = sum([m * int(c) for m, c in zip(cycle((1,3)), isbn[:12])]) % 10
    return 0 if x == 0 else 10 - x


print(isbn_checkdigit("978030640615"))
print(isbn_checkdigit2("978030640615"))
print(isbn_checkdigit3("978030640615"))
# print(isbn_checkdigit("978974443626"))
# print(isbn_checkdigit("978039307295"))
# print(isbn_checkdigit2("978039307295"))
# print(isbn_checkdigit3("978039307295"))
# a = (1, 3) * 6
# print(a)