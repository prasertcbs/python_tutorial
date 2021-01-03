def mtable(fromN=2, toN=6):
    for i in range(1, 13):
        for j in range(fromN, toN + 1):
            print("{:2} x {:2} = {:3} | ".format(j, i, j * i), end="")
        print()


if __name__ == '__main__':
    # fromN = int(input("from:"))
    # toN = int(input("to:"))
    # mtable(fromN, toN)
    mtable()