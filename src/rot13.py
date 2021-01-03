# https://th.wikipedia.org/wiki/ROT13
def rot13(s):
    d = []
    for c in s:
        if c.upper() in   "ABCDEFGHIJKLM":
            d.append(chr(ord(c) + 13))
        elif c.upper() in "NOPQRSTUVWXYZ":
            d.append(chr(ord(c) - 13))
        else:
            d.append(c)
    return "".join(d)

# print(ord("A"), chr(65))
# print(ord("A") + 13, chr(78))
print(rot13("HELLO"))
print(rot13("Python"))
print(rot13("URYYB"))
