def demo2():
    m = {"th": [5, 3, 7],
         "sg": [3, 1, 2]}
    print(m)
    print(m["th"])
    print(m["th"][0])
    print(m["th"][0] + m["th"][1] + m["th"][2])


def demo3():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 1, "b": 2},
        "jp": {"g": 13, "s": 10, "b": 25}
    }
    print(m)
    print(m["th"])
    print(m["th"]["b"])
    print(m["th"]["g"] + m["th"]["s"] + m["th"]["b"])


def loop_dict():
    m = {
        "th": {"g": 5, "s": 3, "b": 7},
        "sg": {"g": 3, "s": 1, "b": 2},
        "jp": {"g": 13, "s": 10, "b": 25}
    }
    print(m.keys())
    for c in sorted(m.keys()):  # keys
        print(c)
    print("-" * 40)
    for c in m.keys():  # keys
        print(c)
    print("-" * 40)
    for c in m.values():
        print(c)
    print("-" * 40)
    for k, v in m.items():
        print("key={}, value={}".format(k, v))


# demo3()
loop_dict()
