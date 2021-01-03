import random


def fx(op):
    if op == '+':
        return lambda a, b: a + b
    else:
        return lambda a, b: a - b


def fx2(op):
    # inner function
    def add(a, b): return a + b

    def subtract(a, b):
        return a - b
    if op == '+':
        return add
    else:
        return subtract


def fx3(op):
    d = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b
    }
    return d[op]


if __name__ == "__main__":
    # func=fx2('+')
    # print(func(5, 3))
    # func=fx3('*')
    # print(func(5, 3))
    for _ in range(5):
        op = random.choice(['+', '-', '*', '/', '^'])
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        func = fx3(op)
        print(f'{a:3} {op} {b:3} = {func(a, b):7}')
