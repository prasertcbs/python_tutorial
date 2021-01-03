def hide_chars(s, fromPos, toPos):
    lst = []
    for i, c in enumerate(s):
        # print(i, c)
        if i in range(fromPos, toPos + 1):
            if c == ' ':
                lst.append(c)
            else:
                lst.append('x')
        else:
            lst.append(c)
    # print(lst)
    return ''.join(lst)


if __name__ == '__main__':
    s = "superhero@zeromail.com"
    print(s, "---> ", hide_chars(s, 2, 7))
    s = "0841234567"
    print(s, "---> ", hide_chars(s, 2, 6))
    s = "4402 1234 5678 9012"
    print(s, "---> ", hide_chars(s, 5, 12))
