def name_freq():
    d = {}
    with open("thai_provinces.csv", encoding='utf8', newline='') as f:
        for i, line in enumerate(f):
            if i > 0:
                p = line.strip().split(',')
                # print(p[2][0])
                name = p[2][0]
                if name in d:
                    d[name] += 1
                else:
                    d[name] = 1
    return d

if __name__ == '__main__':
    d = name_freq()
    # for k, v in d.items():
    #     print("{} = {:2}:{}".format(k, v, '*' * v))
    for k in sorted(d.keys()):
        print("{} = {:2}:{}".format(k, d[k], '*' * d[k]))
    print("total = {}".format(sum(d.values())))