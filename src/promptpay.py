def basic():
    # input
    amt = 320000

    # process
    fee = 0
    if amt <= 5000:
        fee = 0
    # elif amt > 5000 and amt <= 30000:
    elif 5000 < amt <= 30000:
        fee = 2
    elif 30000 < amt <= 100000:
        fee = 5
    else:
        fee = 10

    # output
    print("fee = ", fee)


def basic2():
    # amt = 600000
    # input
    amt = float(input("transfer amount: "))

    # process
    fee = 0

    if amt > 100000:
        fee = 10
    elif amt > 30000:
        fee = 5
    elif amt > 5000:
        fee = 2
    else:
        fee = 0

    # output
    print("fee = ", fee)


if __name__ == '__main__':
    basic2()
