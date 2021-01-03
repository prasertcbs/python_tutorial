# strip / trim
def demo_strip():
    s = "Thai land"
    t = "  Thai land  "
    u = t.strip()

    print(s == t)
    print(s == u)

def demo_isdigit(p):
    total = 0
    for c in p:
        # print(c)
        if c.isdigit():
            # print(c)
            total += int(c)
    return total


def remove_non_digit(s):
    t = ""
    for c in s:
        if c.isdigit():
            t += c
            # t = t + c
    return t

# plate = "1กท 4567"
# print(demo_isdigit(plate))

card_id = "(068)345-6789"
print(remove_non_digit(card_id))