# map

def demo1():
    flowers = ['lily', 'carnation', 'jasmine', 'rose', 'tulip']
    flowers2 = list(map(str.capitalize, flowers))
    flowers3 = [f.capitalize() for f in flowers]
    print(flowers2)
    print(flowers3)


def thb2usd(thb):
    return thb * 33


def demo2():
    price_usd = [10, 30, 70, 100]
    price_thb = [n * 33 for n in price_usd]
    price_thb2 = list(map(lambda n: n * 33, price_usd))
    price_thb3 = list(map(thb2usd, price_usd))
    print(price_thb)
    print(price_thb2)
    print(price_thb3)


def area():
    # 2-3-70
    s = input("rai-ngan-sqwah: ").split('-')
    print(s)
    # lst_n = list(map(int, s))
    # print(lst_n)
    rai, ngan, sqwah = list(map(int, s))
    print(rai, ngan, sqwah)
    total_sqwah = rai * 400 + ngan * 100 + sqwah
    print(total_sqwah)


def area2():
    rai, ngan, sqwah = list(map(int, input("rai-ngan-sqwah: ").split('-')))
    return rai * 400 + ngan * 100 + sqwah


if __name__ == '__main__':
    # demo1()
    # demo2()
    # area()
    print(area2())
