def demo():
    print("{}{}".format("th", "Thailand"))
    print("{:5}|{:15}|".format("th", "Thailand"))    # align left
    print("{:<5}|{:<15}|".format("th", "Thailand"))    # align left
    print("{:>5}|{:>15}|".format("th", "Thailand"))  # align right
    print("{:*>5}|{:->15}|".format("th", "Thailand"))  # align right
    print("{:^5}|{:^15}|".format("th", "Thailand"))  # align center

def mult_table(n):
    for i in range(1, 13):
        print("{} x {:2} = {:3}".format(n, i, n * i))

def ascii_table():
    for i in range(65, 128):
        print("{0:3} {0:#08b} {0:04o} {0:#x} {0:X} {0:c}".format(i))

def demo_dict():
    menu = {"name": "mocha", "price": 40, "size": "m"}
    print(menu["name"])
    print("menu name = {} price = {}".format(menu["name"], menu["price"]))
    print("menu name = {name}({size}) price = {price}".format(**menu))



# demo()
# demo_dict()
# mult_table(12)
ascii_table()