# s = "peter"
# print(s.capitalize())
# print(s.upper())
# t = "PARKER"
# print(t.lower())
def demo_upper():
    choice = input("[M]ale, [F]emale: ")
    if choice.upper() == "M":
    # if choice == "M" or choice == "m":
        print("male")
    else:
        print("female")

def demo_title():
    s = "the land of smiles"
    print(s.title())

def demo_split():
    s = "the land of smiles"
    a = s.split()
    print(a)
    print(a[1])
    t = "thailand,5,7,3"
    b = t.split(",")
    print(b)
    x ="1920x1080"
    p = x.split("x")
    print(p)
    w,h=x.split("x")
    print(w, h)

def demo_split_app():
    first_name, last_name = input("enter your full name: ").split()
    print("first name:", first_name)
    print("last name: ", last_name)

# demo_upper()
# demo_title()
# demo_split()
demo_split_app()
