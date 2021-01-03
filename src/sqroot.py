# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

def sqroot(s):
    x0 = s / 2
    # x0 = 600
    x1 = 0
    precision = .000001
    delta = 1
    while delta > precision:
        x1 = .5 * (x0 + s / x0)
        delta = abs(x1 - x0)
        print("x0 = {:.7f}, x1 = {:.7f}, delta = {:.7f}".format(x0, x1, delta))
        x0 = x1
    return x1


if __name__ == '__main__':
    n = 125348
    x = sqroot(n)
    print("x = {}, x**2 = {}".format(x, x ** 2))
