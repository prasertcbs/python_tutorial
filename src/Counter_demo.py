from collections import Counter


def tally():
    orders = ["mocha", "latte", "mocha", "espresso", "americano", "latte", "mocha", "espresso"]
    cnt = {}
    for s in orders:
        if s in cnt:
            cnt[s] += 1
        else:
            cnt[s] = 1
    print(cnt)

def tally_Counter():
    orders = ["mocha", "latte", "mocha", "espresso", "americano", "latte", "mocha", "espresso"]
    cnt = Counter(orders)
    print(cnt)
    print(cnt["latte"])

def tally2():
    # s = "HHTHHHTHTTTHTHTTTHTT"
    s = "somewhere over the rainbow way up high"
    cnt = Counter(s)
    print(cnt)
    # print(cnt.most_common(3))
    # print(cnt.most_common(3)[1][0])
    del cnt[" "]
    print(cnt)


# tally()
# tally_Counter()
tally2()