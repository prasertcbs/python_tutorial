# type hints
from datetime import date


def alpha(a, b): # dynamic typed
    c = a + b
    print(c)

def beta(a: str, b: int, c):
    # print(a.upper())
    print(a, b, c)

def gamma(a: date, b):
    print(a.year)
    print(b.year)

def bar(a, b) -> str:
    return a + b

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def foo(self):
        print("hello")

def epsilon(a: Person, b):
    a.foo()


if __name__ == '__main__':
    # alpha(5, 3)
    # alpha("rain", "bow")
    # beta(3, "bow", 77)
    # t1 = date(2016, 7, 20)
    # t2 = date(2017, 1, 9)
    # gamma(t1, t2)
    p = Person("Peter", "Parker", 26)