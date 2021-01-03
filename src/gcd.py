def gcd1(a, b):
    d = a if a < b else b # min(a, b)
    for i in range(d, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# algorithm
def gcd2(a, b):
    """
    ref: https://en.wikipedia.org/wiki/Euclidean_algorithm#Euclidean_division
    function gcd(a, b)
    while b ≠ 0
       t := b;
       b := a mod b;
       a := t;
    return a;
    :param a:
    :param b:
    :return:
    """
    while b != 0:
        # t = b
        # b = a % b
        # a = t
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd2(a, b)

# print(gcd1(12, 6))
# print(gcd1(120, 45))
# print(gcd2(77, 33))
print(lcm(10,5))