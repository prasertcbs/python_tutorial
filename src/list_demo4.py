def demo():
    flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
    # is_exist = "daisy" in flowers
    # is_exist = "Lily" in flowers
    # print(is_exist)

    # print(flowers.index("lily"))
    # print(flowers.index("daisy"))

    flowers[2] = "Jasmine"
    print(flowers)
    for i in range(len(flowers)):
        flowers[i] = flowers[i].capitalize()
    print(flowers)
    flowers.clear()
    print(flowers)

def demo_append():
    countries = [
        ("th", "Thailand", "ไทย"),
        ("jp", "Japan", "ญี่ปุ่น"),
        ("kr", "Korea", "เกาหลีใต้")
    ]
    print(countries)
    fr = ("fr", "France", "ฝรั่งเศส")
    countries.append(fr)
    print(countries)
    us = ("us", "USA", "อเมริกา")
    countries.insert(2, us)
    print(countries)
    countries.append(("sg", "Singapore", "สิงคโปร์"))
    print(countries)

# demo()
# demo_append()
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet)
a = [0] * 10
print(a)
b = [1, 3] * 5
print(b)