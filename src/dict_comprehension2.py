import csv


def nato_from_file():
    with open("nato.txt") as f:
        d = {line[0]:line[:-1] for line in f}
        return d

def convert(s):
    d = nato_from_file()
    r = [d[c.upper()] for c in s]
    return " ".join(r)

def abbr_province_dict():
    with open("abbr_province.txt", encoding="utf8") as f:
        data = csv.reader(f)
        d = {k:v for k, v in data}
        return d

# print(nato_from_file())
# print(convert("python"))
p = abbr_province_dict()
print(p)
print(p["ชพ"])
