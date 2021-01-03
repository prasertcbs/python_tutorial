def dec_to_bin(n):
    # ref: http://www.purplemath.com/modules/numbbase.htm
    x = n
    s = ""
    base = 2
    while x > 0:
        s += str(x % base)
        x = x // base
    # print(s)
    # print(s[::-1])
    return s[::-1]


print(dec_to_bin(357))    # postfix completion
print("{0} {0:b} {0:o}".format(357))