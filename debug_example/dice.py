import random

def roll():
    for i in range(100):
        d1=random.randint(1, 6)
        d2=random.randint(1, 6)
        total=d1+d2
        print(f'{d1} + {d2} = {total}')

if __name__ == "__main__":
    roll()