# 4597 7692 1332 987
#  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |
#  4 | 5 | 9 | 7 | 7 | 6 | 9 | 2 | 1 | 3 | 3 | 2 | 9 | 8 | 7 |
#  2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
# ------------------------------------------------------------
#  8 | 5 |18 | 7 |14 | 6 |18 | 2 | 2 | 3 | 6 | 2 |18 | 8 |14 |
#  8 | 5 | 9 | 7 | 5 | 6 | 9 | 2 | 2 | 3 | 6 | 2 | 9 | 8 | 5 |
# sum = 86
# check digit = 4

def remove_non_digit(s):
    # d = []
    # for c in s:
    #     if c.isdigit():
    #         d.append(int(c))
    # return d
    return [int(c) for c in s if c.isdigit()]


def print_digit(v):
    # for i in v:
    #     print("{:>2} |".format(i), end="")
    [print("{:>2} |".format(i), end="") for i in v]
    print()


if __name__ == '__main__':
    card = "4597 7692 1332 987"
    print(card)
    card = remove_non_digit(card)
    print_digit(range(15))  # [0, 14]
    print_digit(card)
    a = [2, 1] * 7 + [2]
    print_digit(a)
    print("-" * 70)
    y = [m * n for m, n in zip(card, a)]
    print_digit(y)
    y2 = [n if n < 10 else n // 10 + n % 10 for n in y]
    print_digit(y2)
    sum_y2 = sum(y2)
    print("sum = {}".format(sum_y2))
    # Luhn mod 10
    r = sum_y2 % 10
    chk_digit = 0 if r == 0 else 10 - r
    print("check digit = {}".format(chk_digit))
