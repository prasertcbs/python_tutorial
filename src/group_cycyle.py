from itertools import cycle


def demo1():
    # แบ่งทีมออกเป็นกลุ่ม ๆ หรือแยกเป็นสี ๆ
    students = ["Napaphat", "Thorfan", "Thatchaphon", "Nareerat",
                "Pimchanok", "Ruj", "Kodchanon", "Kamolthip",
                "Koraphat", "Kunratchaviya", "Kanlaya", "Janejira",
                "Jalernwut", "Chatchat", "Chanyanuch", "Naphat",
                "Natcha", "Nattida", "Nat", "Duangjanchay"]
    colors = ["red", "green", "yellow", "blue", "pink", "orange"]
    d = {c: [] for c in colors}
    for s, c in zip(students, cycle(colors)):
        d[c].append(s)
    # print(d)
    for k,v in d.items():
        print("{}: {}".format(k, v))
    # [print(e) for e in zip(students, cycle(colors))]
    # print(colors * 4)
    # [print(e) for e in zip(students, colors * 4)]


demo1()

