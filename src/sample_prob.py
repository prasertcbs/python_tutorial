import random
from collections import Counter


def sample_prob1():
    choices = ["dog"] * 65 + ["cat"] * 25 + ["fish"] * 10
    print(choices)
    a = [random.choice(choices) for i in range(10)]
    print(a)

def sample_prob2():
    cnt = Counter(dog=65, cat=25, fish=10)
    choices = list(cnt.elements())
    print(choices)
    a = [random.choice(choices) for i in range(10)]
    print(a)

def sample(choices, size):
    l = list(choices.elements())
    a = [random.choice(l) for i in range(size)]
    return a

# sample_prob1()
# sample_prob2()

x = sample(Counter(dog=65, cat=25, fish=10), 20)
print(x)