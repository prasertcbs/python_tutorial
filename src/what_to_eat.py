import random

def read_menu(filename='food_menu.txt'):
    with open(filename, encoding='utf8') as f:
        s=f.readlines()
    menus=[e.strip() for e in s]
    return menus

if __name__ == "__main__":
    # print(read_menu())
    menus=read_menu()
    # m=random.choice(menus)
    while True:
        k=int(input('จำนวนเมนู: '))
        if k==0:
            break
        m=random.choices(menus, k=k)
        print(m)