def rectangle(w, h):
    return w * h

rect=lambda w, h: w * h
triangle=lambda w, h: w * h * .5

def area(func, w, h):
    return func(w, h)

def usd_thb(v):
    return v * 32

# map, filter, reduce
# apply (pandas)
def demo1():
    usd = [10, 12, 20, 8]
    thb = list(map(lambda v: v * 32, usd))
    thb2 = list(map(usd_thb, usd))
    print(thb)
    print(thb2)

if __name__ == "__main__":
    # print(rectangle(5, 10))
    # print(rect(5, 10))
    # print(area(rect, 5, 10))
    # print(area(triangle, 5, 10))
    demo1()
