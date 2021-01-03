def demo1():
    numbers=[10, 15, 7, 8, 2, 9, 4]
    r1=filter(lambda v: v % 2 == 0, numbers)
    print(type(r1))
    print(r1)
    print(list(r1))

def demo2():
    numbers=[10, 15, 7, 8, 2, 9, 4]
    func=lambda v: v % 2 == 0
    func2=lambda v: v % 2 == 1
    r1=filter(func2, numbers)
    print(type(r1))
    print(r1)
    print(list(r1))

def demo3():
    flowers=['lily', 'rose', 'sakura', 'carnation', 'jasmine']
    r1=filter(lambda v: 's' in v, flowers)
    print(list(r1))

def demo4():
    flowers=[['lily', 40], ['rose', 15], ['sakura', 30], ['carnation', 25], ['jasmine', 20]]
    r1=filter(lambda v: v[1] > 20, flowers)
    print(list(r1))
    r2=filter(lambda v: len(v[0]) > 4, flowers)
    print(list(r2))
    l=[v for v in flowers if (len(v[0]) > 4)]
    print(l)
    l2=[v[0] for v in flowers if (len(v[0]) > 4)]
    print(l2)

if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    demo4()