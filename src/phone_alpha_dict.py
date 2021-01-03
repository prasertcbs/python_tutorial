def reg_phone(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric = "22233344455566677778889999"
    s = s.upper()
    x = ""
    for c in s:
        if c in alphabet:
            x += numeric[alphabet.index(c)]
        else:
            x += c
    return x


def reg_phone2(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric =  "22233344455566677778889999"
    s = s.upper()
    x = [numeric[alphabet.index(c)] if c in alphabet else c for c in s]
    return "".join(x)

def gen_keypad():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric =  "22233344455566677778889999"
    x = ["{!r}:{!r}".format(a, b) for a, b in zip(alphabet, numeric)]
    # print(x)
    return ",\n".join(x)

def reg_phone_dict(s):
    d = {
        'A': '2',
        'B': '2',
        'C': '2',
        'D': '3',
        'E': '3',
        'F': '3',
        'G': '4',
        'H': '4',
        'I': '4',
        'J': '5',
        'K': '5',
        'L': '5',
        'M': '6',
        'N': '6',
        'O': '6',
        'P': '7',
        'Q': '7',
        'R': '7',
        'S': '7',
        'T': '8',
        'U': '8',
        'V': '8',
        'W': '9',
        'X': '9',
        'Y': '9',
        'Z': '9'
    }
    s = s.upper()
    x = [d[c] if c in d else c for c in s]
    return "".join(x)
    # x = ""
    # for c in s:
    #     if c in d:
    #         x += d[c]
    #     else:
    #         x += c
    # return x

if __name__ == '__main__':
    p = "000yinyang"
    print(reg_phone(p))
    print(reg_phone2(p))
    print(reg_phone_dict(p))
    # print(gen_keypad())
