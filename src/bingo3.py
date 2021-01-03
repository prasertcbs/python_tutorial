import random

import time

def bingo_card3(n_col=5):
    n = random.sample(range(1, 100), n_col * n_col)
    # print(n)
    for i, v in enumerate(n):
        # print(i, v)
        if (i % n_col == 0) and (i != 0):
            print()
        if i == n_col * n_col // 2:
            print("{:>5}".format("FS"), end="")
        else:
            print("{:5}".format(v), end="")
    print()

def call_number():
    n = random.sample(range(1, 100), 99)
    for i in n:
        print(i, end="")
        # time.sleep(.5)
        c = input()
        if c == 'q':
            break

def call_number_yield():
    n = random.sample(range(1, 100), 99)
    for i in n:
        yield i

if __name__ == '__main__':
    for i in range(4):
        bingo_card3(7)
        print("-" * 40)
    n = call_number_yield()
    print("press enter to call a next number (q to quit) ")
    while input().upper() != "Q":
        try:
            print(next(n), end="")
        except:
            break
    print("the end.")