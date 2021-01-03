def demo():
    skills = {"Python", "C", "Java"}
    print(skills)
    print(type(skills))
    a = {} # dictionary
    print("type a = ", type(a))
    b = set()
    print("type b = ", type(b))
    xy = {(3,7), (5, 10), (15, 9)}    # tuple -> immutable -> hashable
    print(xy)
    countries = {["Thailand", "Bangkok"], ["Japan", "Tokyo"]}   # list -> mutable -> unhashable
    print(countries)

def basic_op():
    a = {"mango", "banana", "coconut", "mango", "apple"}
    print("a =", a)
    b = {"cherry", "mango", "apple"}
    m = a | b    # union
    print(m)
    n = a & b
    print(n)
    p = a - b
    print(p)
    q = a ^ b # symmetric difference  (a union b) - (a intersect b)
    print(q)

# demo()
basic_op()