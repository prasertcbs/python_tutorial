def demo_reader():
    f = open("flower.txt")
    data = f.read()
    print(data)
    f.close()

def demo_readline():
    f = open("flower.txt")
    data = f.readline()
    print(data)
    data2 = f.readline()
    print(data2)
    f.close()

def demo_readlines():
    f = open("flower.txt")
    data = f.readlines()
    print(data)
    f.close()

def demo_readline2():
    f = open("flower.txt")
    for i in range(3):
        print(f.readline(), end="")
    f.close()

def demo_readlines2():
    f = open("flower.txt")
    for line in f:
        print(line.capitalize(), end="")
    f.close()

# demo_reader()
# demo_readline()
# demo_readlines()
# demo_readline2()
demo_readlines2()