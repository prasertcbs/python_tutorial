def demo_reader():
    with open("flower.txt", mode="r") as f:
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader2():
    with open("c:/data/flower.txt", mode="r",encoding="utf8") as f:
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_unicode():
    with open("c:/data/province.txt", mode="r", encoding="utf8") as f:
        print(f.name)
        print(f.mode)
        data = f.read()
        print(data)

def demo_reader_unicode2():
    with open("c:/data/province.txt", mode="r", encoding="utf8") as f:
        # i = 1
        # for line in f:
        #     print("{}. {}".format(i, line), end="")
        #     i = i + 1
        for i, line in enumerate(f):
            print("{}. {}".format(i+1, line), end="")


# demo_reader()
# demo_reader2()
# demo_reader_unicode()
demo_reader_unicode2()