def fv(p, period, rate):
    return p * (1+rate) ** period

def pv(p, period, rate):
    return p / (1+rate) ** period

def print_table():
    # periods=range(1, 11)
    periods=list(range(1, 11)) + list(range(15, 41, 5))
    rates=range(1, 11)
    print('period', end='')
    for r in rates:
        print(f'{r:>7}%', end='')
    print()
    for p in periods:
        print(f'{p:>6}', end='')
        for r in rates:
            print(f'{fv(1, p, r/100):>8.4f}', end='')
        print()

if __name__ == "__main__":
    # print(fv(1, 5, .01))
    # x = list(range(1, 11))
    # y = list(range(15, 41, 5))
    # print(x)
    # print(y)
    # print(x + y)
    print_table()