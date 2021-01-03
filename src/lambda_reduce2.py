from functools import reduce

def demo_reduce_logic():
    age = 15
    gender = 'F'
    height = 165
    weight = 48
    crit = [age > 18, gender == 'F', height > 160, weight > 45]
    ok = reduce(lambda cv, v: cv and v, crit)
    # ok = crit[0] and crit[1] and crit[2] and crit[3]
    print(ok)

def demo_join_list():
    sep='|'
    names=['Peter', 'Jenny', 'Linda', 'Bruce', 'Ann']
    print(sep.join(names))
    x = reduce(lambda cv, v: f'{cv}{sep}{v}', names)
    print(x)

def demo_if_reduce():
    numbers = [3, 6, 4, 1, 7, 8]
    # sum even numbers
    x = reduce(lambda cv, v: cv + (v if v % 2 == 0 else 0), numbers, 0)
    # x = reduce(lambda cv, v: cv + (v if v % 2 == 0 else 0), numbers)
    print(x)

def demo_list_dict():
    names = [
        {'name': 'Peter', 'score': 5},
        {'name': 'Ann', 'score': 8},
        {'name': 'Jenny', 'score': 7},
        {'name': 'Bruce', 'score': 10}
    ]
    x = reduce(lambda cv, v: cv + v['score'], names, 0)
    # x = reduce(lambda cv, v: cv + v['score'], names)
    print(x)
    print(sum([v['score'] for v in names]))

if __name__ == "__main__":
    # demo_reduce_logic()
    # demo_join_list()
    # demo_if_reduce()
    demo_list_dict()