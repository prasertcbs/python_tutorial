import sys

def tis2utf(tis: str) -> str:
    s = ""
    for c in tis:
        if 0xa0 <= ord(c) <= 0xfb:
            s += chr(ord(c) + 0xe00 - 0xa0)
        else:
            s += c
    return s

def tis2utfv2(tis: str) -> str:
    s = [chr(ord(c) + 0xe00 - 0xa0) if 0xa0 <= ord(c) <= 0xfb else c for c in tis]
    return "".join(s)

def convert_file_tis2utf(tis_input, utf_output):
    tis = ""
    with open(tis_input, encoding="utf-8") as f:
        tis = f.read()
    with open(utf_output, "w", encoding="utf-8") as f:
        f.write(tis2utfv2(tis))

if __name__ == '__main__':
    # s = "hello world »ÃÐà·Èä·Â Thailand เมืองยิ้ม"
    # print(tis2utf(s))
    # print(tis2utfv2(s))
    # convert_file_tis2utf('tis.txt', 'utf.txt')
    convert_file_tis2utf(sys.argv[1], sys.argv[2])
