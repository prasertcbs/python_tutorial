import random


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


if __name__ == '__main__':
    for i in range(4):
        bingo_card()
        print()
        print("-" * 40)