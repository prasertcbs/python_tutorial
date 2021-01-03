def loop1():
    for i in range(11): # for(i=0;i<11;i++)
        print(i)

def loop2():
    for i in range(1, 11):
        print(i)

def loop3():
    for i in range(1, 11, 2):
        print(i)
        print("-------------")
    print("bye")

def loop_string():
    s = "over the rainbow"
    for c in s: # for each
        print(c.upper())

def loop_tuple():
    flowers = "lily", "jasmine", "rose", "ivy"
    for f in flowers:
        print(f.capitalize())

def loop_tuple2():
    flowers = "lily", "jasmine", "rose", "ivy"
    for i in range(len(flowers)):
        print(i+1, flowers[i].capitalize(), sep=". ")

loop3()
# loop_string()
# loop_tuple()
# loop_tuple2()