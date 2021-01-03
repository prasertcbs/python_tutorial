def display_keypad():
    k=[
        ('1', ''),
        ('2', 'ABC'),
        ('3', 'DEF'),
        ('4', 'GHI'),
        ('5', 'JKL'),
        ('6', 'MNO'),
        ('7', 'PQRS'),
        ('8', 'TUV'),
        ('9', 'WXYZ'),
        ('*', ''),
        ('0', '+'),
        ('#', '')
    ]
    # print(k)
    row=4
    col=3
    print('-' * 25)
    for r in range(row):
        for c in range(col):
            print(f'|{k[r*col+c][0]:^7}', end='')
        print('|')
        for c in range(col):
            print(f'|{k[r*col+c][1]:^7}', end='')
        print('|')
        print('-' * 25)

if __name__ == "__main__":
    display_keypad()