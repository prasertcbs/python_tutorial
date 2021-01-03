# generators / yield

def station():
    yield "HUA"
    yield "SAM"
    yield "SIL"
    yield "LUM"


def sum_all_digit(n):
    return sum([int(c) for c in str(n)])


def lucky(target=9, start_num=1, stop_num=100):
    d = []
    for i in range(start_num, stop_num + 1):
        if sum_all_digit(i) == target:
            d.append(i)
    return d


def luck_gen(target=9, start_num=1):
    i = start_num
    while True:
        if sum_all_digit(i) == target:
            yield i
        i += 1


def zip_demo():
    pretest = [5, 7, 4, 8, 10]
    posttest = [6, 7, 5, 10, 9]
    z = zip(pretest, posttest)
    print(next(z))
    print("-" * 80)
    for i, j in z:
        print(i, j)
    print("-" * 80)
    print(next(z))


zip_demo()
# print(lucky(8, 1, 100))
# g = luck_gen(8, 1000)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# s = station()
# print(s)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
