def ticket(age):
    if age <=5:
        return 0
    else:
        return 100

def ticket2(age):
    if age <=5 or age >= 60:
        return 0
    else:
        return 100

def ticket2a(age):
    return 0 if age <=5 or age >= 60 else 100 # ternary
    # return age <=5 || age >= 60 ? 0 : 100; # java

def ticket3(age, is_local):
    if (age <=5 or age >= 60) and is_local:
        return 0
    else:
        return 100

def demo(a):
    if a >=10 and a <= 20:
        print("ok")
    else:
        print("not ok")

def demo2(a):
    if 10 <= a <= 20:
        print("ok")
    else:
        print("not ok")

demo2(18)

print(ticket(4))
print(ticket2(70))
print(ticket2(35))
print(ticket2(3))
print(ticket3(3, False))
