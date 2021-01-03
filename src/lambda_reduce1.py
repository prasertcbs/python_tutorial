from functools import reduce

def demo1():
    n=range(1, 6)
    sum = 0
    for i in n:
        sum += i
    return sum

def demo1r():
    n=range(1, 6)
    sum=reduce(lambda cv, v: cv + v, n)
    return sum

def demo2r():
    n=range(1, 6)
    sum=reduce(lambda cv, v: cv + v, n, 0)
    return sum

def factorial(n):
    fact=reduce(lambda cv, v: cv * v, range(1, n+1), 1)
    return fact

def factorial2(n):
    f=1
    for i in range(1, n + 1):
        f *= i
    return f

if __name__ == "__main__":
    # print(demo1())
    # print(demo1r())
    # print(demo2r())
    print(factorial(5)) # 1 * 2 * 3 * 4 * 5
    print(factorial2(5)) # 1 * 2 * 3 * 4 * 5