# print(3, 5, 10)
# print(3, 10)
# print(2, "two", 3, 10, 5, True, 99)

def avg(*args):
    print(type(args))
    print(args)
    print(args[3])
    total = 0
    for i in args:
        total += i
    return total / len(args)


def print_bullet(*items, bullet="\u2022"):
    for e in items:
        print("{} {}".format(bullet, e))

# print(avg(4, 7, 8, 12, 9))
# print(4, 7, 8, 12, 9, sep="-")

print_bullet("lily", "rose", "jasmine", "forget me not", bullet="+")