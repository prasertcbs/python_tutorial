from collections import namedtuple


def demo1():
    x = (4, 7, 8)
    print("x = ", x)
    Medal = namedtuple("Medal", ["gold", "silver", "bronze"])
    th = Medal(4, 7, 8)
    print("th = ", th)
    print(th.gold)
    print(sum(th[:2]))

def demo2():
    Medal = namedtuple("Medal", ["country", "gold", "silver", "bronze"])
    th = Medal("Thailand", 4, 7, 8)
    print(th.country)
    print(sum(th[1:]))

def demo3():
    Medal = namedtuple("Medal", "country gold silver bronze")
    th = Medal("Thailand", 4, 7, 8)
    print(th)
    kr = Medal(country = "Korea", bronze=10, gold=15, silver=7)
    print(kr)
    j = ("Japan", 30, 20, 10)
    jp = Medal._make(j)
    print(jp)
    od = jp._asdict()
    print(od)

def demo4():
    Area = namedtuple("RaiNganSqwa", "rai ngan sqwa")
    area1 = Area(3, 2, 70)
    print(area1)
    total_area = area1.rai * 400 + area1.ngan * 100 + area1.sqwa
    print(total_area)

# demo1()
# demo2()
# demo3()
demo4()