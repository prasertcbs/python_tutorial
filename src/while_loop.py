def demo1():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("bye")

def demo_for():
    for i in range(1, 11):
        print(i)
    print("bye")

def sum_input():
    n = int(input("enter number: "))
    total = 0
    while n != 0:
        total += n
        n = int(input("enter number: "))
    print("total = ", total)

def sum_input_repeat_unit():
    total = 0
    while True:
        n = int(input("enter number: "))
        if n != 0:
            total += n
        else:
            break
    print("total = ", total)


# repeat until
# do ... while
# demo1()
# demo_for()
# sum_input()
sum_input_repeat_unit()