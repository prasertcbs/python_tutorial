def v1():
    for i in range(1, 11):
        print(i, i * 0.621371192)


def v2():  # list comprehension
    [print(i, i * 0.621371192) for i in range(1, 11)]
    m = [i * 0.621371192 for i in range(1, 11)]
    n = [km_mi(i) for i in range(1, 11)]
    print(m)
    print(n)


def v3():  # lambda
    m = list(map((lambda i: i * 0.621371192), range(1, 11)))
    print(m)


def km_mi(k):
    return k * 0.621371192


# v1()
v2()
# v3()
