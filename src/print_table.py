def demo1():
    data=list(range(0, 12))
    row=3
    col=4
    for r in range(row): # 0, 1, 2
        for c in range(col): # 0, 1, 2, 3
            print(f'{data[r*col+c]:5}', end='')
        print()

def demo2():
    data=list(range(1, 21))
    row=4
    col=5
    for r in range(row): 
        for c in range(col): 
            print(f'{data[r*col+c]:5}', end='')
        print()

def demo3():
    data=list("ABCDEFGHIJKL")
    row=2
    col=6
    for r in range(row): 
        for c in range(col): 
            print(f'{data[r*col+c]:5}', end='')
        print()

def demo4():
    data=['January', 'February', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'September', 'Oct', 'November', 'Dec']
    row=4
    col=3
    for r in range(row): 
        for c in range(col): 
            print(f'{data[r*col+c]:^13}', end='')
        print()
        
if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    demo4()
