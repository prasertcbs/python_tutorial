import random

import time


def bingo_card():
    n = list(range(1, 26))
    # print(n)
    random.shuffle(n)
    # print(n)
    for i, v in enumerate(n):
        # print(i, v)
        if (i % 5 == 0) and (i != 0):
            print()
        if i == 25 // 2:
            print("  FS", end="")
        else:
            print("{:4}".format(v), end="")
    print()


def bingo_card2():
    n = random.sample(range(1000, 9999), 25)
    # print(n)
    for i, v in enumerate(n):
        # print(i, v)
        if (i % 5 == 0) and (i != 0):
            print()
        if i == 25 // 2:
            print("{:>5}".format("FS"), end="")
        else:
            print("{:5}".format(v), end="")
    print()


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

if __name__ == '__main__':
    for i in range(4):
        bingo_card3(7)
        print("-" * 40)
    call_number()