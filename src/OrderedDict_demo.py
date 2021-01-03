# OrderedDict
from collections import OrderedDict


def demo1():
    d = {}
    d["A"] = "Alpha"
    d["B"] = "Beta"
    d["C"] = "Charlie"
    d["D"] = "Delta"
    print(d)
    od = OrderedDict()
    od["A"] = "Alpha"
    od["B"] = "Beta"
    od["C"] = "Charlie"
    od["D"] = "Delta"
    print(od)
    od1 = OrderedDict([('A', 'Alpha'), ('B', 'Beta'), ('C', 'Charlie'), ('D', 'Delta')])
    print(od1)
    print(od["B"])
    if "C" in od:
        print(od["C"])
    else:
        print("not found")
    print(od.keys())
    print(od.values())
    print(od.items())

def demo2():
    d = {}
    d["A"] = "Alpha"
    d["B"] = "Beta"
    d["C"] = "Charlie"
    d["D"] = "Delta"
    sd = sorted(d.items())
    print(sd)
    od = OrderedDict(sorted(d.items()))
    print(od)
    for k, v in od.items():
        print("key = {}, value = {}".format(k, v))

def nato(s):
    p = OrderedDict()
    with open("nato.txt") as f:
        for line in f:
            p[line[0]] = line.strip()
    # print(p)
    # for k, v in p.items():
    #     print("{}: {}".format(k, v))
    return " ".join([p[c.upper()] if c.upper() in p else c for c in s])
# demo1()
# demo2()
print(nato("hello world"))