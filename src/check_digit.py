# https://th.wikipedia.org/wiki/เลขประจำตัวประชาชนไทย
def thai_id_checkdigit1(id_num):
    m = 13
    total = 0
    for c in id_num[:12]:
        total += int(c) * m
        m -= 1
    x = total % 11
    return 1 - x if x <= 1 else 11 - x


def thai_id_checkdigit2(id_num):
    total = sum([int(c) * (13 - i) for i, c in enumerate(id_num[:12])])
    x = total % 11
    return 1 - x if x <= 1 else 11 - x


def thai_id_checkdigit3(id_num):
    total = sum([int(c) * i for i, c in zip(range(13, 1, -1), id_num[:12])])
    x = total % 11
    return 1 - x if x <= 1 else 11 - x


print(thai_id_checkdigit1("123456789012"))
print(thai_id_checkdigit2("123456789012"))
print(thai_id_checkdigit3("123456789012"))
