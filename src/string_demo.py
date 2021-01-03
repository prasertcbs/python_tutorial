# s = "rain"
# t = 'bow'
# print(s)
# print(t)
# print(s + t)
# print("-" * 20)
# line = "<>" * 10
# print(line)
# a = s + t
# print(a)
# print("Bow"  in a)

def slice():
    r = "0123456"
    s = "rainbow"
    # print(s[0])
    # print(s[0:4]) # start:end:step
    # print(s[0:4:2]) # start:end:step
    # print(s[0::2]) # start:end:step
    # print(s[6])
    # print(s[-1])
    print(s[-3:])
    print(s[-7:-3])
    print(s[::-1])    # reverse string

def print_string(s):
    for i in range(len(s)):
        print("{:>3} ".format(i), end="")
    print()
    for i in range(-len(s), 0, 1):
        print("{:>3} ".format(i), end="")
    print()
    for c in s: # sequence type (for each)
        print("{:>3} ".format(c), end="")
    print()

print_string("rainbow")
slice()