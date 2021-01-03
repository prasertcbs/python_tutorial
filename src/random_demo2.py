import random

# print(random.random())
# [print(random.randint(1, 6)) for i in range(10)]
# [print(random.randrange(1, 7)) for i in range(10)]
# [print(random.randrange(0, 20, 2)) for i in range(10)]
# [print(random.choice(["rock", "paper", "scissors"])) for i in range(5)]
# [print(random.choice("HT")) for i in range(5)]
# [print(random.normalvariate(160, 3.5)) for i in range(5)]
flowers = ["lily", "rose", "tulip", "magnolia", "jasmine", "carnation"]
b = random.sample(flowers, 3)
print(b)
# print(flowers)
# random.shuffle(flowers)
# print(flowers)
# [print(random.uniform(1, 10)) for i in range(5)]

