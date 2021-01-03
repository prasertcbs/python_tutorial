import random


def coin_flip():
    return "H" if random.randint(0,1) == 0 else "T"

def roll_dice():
    return random.randint(1, 6)

def atm_pin():
    return "{:06}".format(random.randint(1, 999999))

def password_gen(length):
    s = ""
    for i in range(length):
        s = s + chr(random.randint(ord("A"), ord("Z")))
    return s


def password_gen2(length):
    p = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789+-*/^&%;:.abcde"
    s = ""
    for i in range(length):
        s = s + random.choice(p)
    return s

for i in range(10):
#     # print(coin_flip())
#     # print(roll_dice())
#     print(atm_pin())
    print(password_gen2(8))

# print(ord("Z"))