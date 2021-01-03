import random

def read_quote(filename='quote.psv'):
    with open(filename, encoding='utf8') as f:
        s=f.readlines()
    q=[e.strip().split('|') for e in s]
    # print(q)
    return q

if __name__ == "__main__":
    quotes=read_quote()
    while True:
        q, a=random.choice(quotes)
        print(f'{q}\n\t{a}')
        k=input('more quote [y/n]: ')
        if k.lower()=='n':
            break
    print('Have a nice day. :-D')