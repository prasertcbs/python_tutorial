# zip

def demo1():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    bmi = []
    for i in range(len(weight)):
        bmi.append(weight[i] / (height[i] / 100) ** 2)
    return bmi


def demo2():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    bmi = []
    for w, h in zip(weight, height):
        # print(w, h)
        bmi.append(w / (h / 100) ** 2)
    return bmi


def demo3():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    return [w / (h / 100) ** 2 for w, h in zip(weight, height)]


def demo4():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    name = ["Leo", "Ben", "Peter"]
    return [{n: w / (h / 100) ** 2} for w, h, n in zip(weight, height, name)]


def demo5():
    weight = [70, 60, 48]
    height = [170, 175, 161]
    name = ["Leo", "Jane", "Peter"]
    gender = ["M", "F", "M"]
    return [{n: w / (h / 100) ** 2} for w, h, n, g in zip(weight, height, name, gender) if
            g == "M"]


print(demo1())
print(demo2())
print(demo3())
print(demo4())
print(demo5())
