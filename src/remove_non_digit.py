def remove_non_digit(s):
    temp = []
    for c in s:
        # print(c)
        if c in '0123456789.':
            temp.append(c)
    # print(temp)
    ns = ''.join(temp)
    # print(ns)
    return float(ns)


def remove_non_digit2(s):
    temp = [c for c in s if c in '0123456789.']
    ns = ''.join(temp)
    return float(ns)


def remove_non_digit3(s):
    return float(''.join([c for c in s if c in '0123456789.']))


if __name__ == '__main__':
    s = input('enter a string: ')
    f = remove_non_digit3(s)
    print(f)
    print(f + 10)
