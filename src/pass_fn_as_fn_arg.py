import random

def add(a, b):
    return a + b

def f(func, a, b):
    return func(a, b) 

def fx(func):
    for _ in range(10):
        a=random.randrange(1, 13)
        b=random.randrange(1, 13)
        print(f'{a} op {b} = {func(a, b)}')

def mental_math():
    funcs= {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b
    }
    # print(funcs[op](5, 2))
    op=random.choice(list(funcs.keys()))
    for _ in range(10):
        a=random.randrange(1, 13)
        b=random.randrange(1, 13)
        print(f'{a:2} {op} {b:2} = ')
        # print(f'{a} {op} {b} = {funcs[op](a, b)}')

if __name__ == "__main__":
    # print(add(5, 2))
    # print(f(add, 5, 2))
    # print(f(lambda a, b: a + b, 5, 2))
    # fop=lambda a, b: a + b
    # print(f(fop, 5, 2))
    # fx(add)
    # fx(lambda a, b: a - b)
    # fx(lambda a, b: a * b)
    mental_math()