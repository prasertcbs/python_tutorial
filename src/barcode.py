# http://www.gs1.org/how-calculate-check-digit-manually
# http://www.gs1.org/check-digit-calculator

def checkdigit1(barcode):
    even = sum([int(c) for c in barcode[0:12:2]])
    odd = sum([int(c) for c in barcode[1:12:2]]) * 3
    total = even + odd
    return 0 if total % 10 == 0 else 10 - (total % 10)


def checkdigit2(barcode):
    total = sum(
        [int(c) if i % 2 == 0 else int(c) * 3 for i, c in enumerate(barcode[:12])])
    return 0 if total % 10 == 0 else 10 - (total % 10)


def checkdigit3(barcode):
    total = sum([int(c) * i for i, c in zip((1, 3) * 6, barcode[:12])])
    return 0 if total % 10 == 0 else 10 - (total % 10)


def demo():
    a = (1, 3) * 6
    print(a)


print(checkdigit1("761210005382"))
print(checkdigit2("761210005382"))
print(checkdigit3("761210005382"))
# demo()
