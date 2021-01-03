r = range(10) # (0, 10)  (inclusive, exclusive)
print(r)
print(list(r))
print(len(r))
print(type(r))

r1 = range(5, 20)
print(list(r1))
print("-" * 40)
r2 = range(5, 20, 2)
print(list(r2))

r3 = range(10, 0, -2)
print(list(r3))

r4 = range(-1, -10, 1)
print(list(r4))

r5 = range(-1, -10, -1)
print(list(r5))

n = range(1, 101, 2)
print(list(n))
print(sum(n))