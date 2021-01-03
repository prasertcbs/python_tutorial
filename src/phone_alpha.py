def reg_phone(s):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric =  "22233344455566677778889999"
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

if __name__ == '__main__':
    p = "081callCBS"
    print(reg_phone(p))
    print(reg_phone2(p))