# print("a")
# print(ord("a"))
# print(ord("A"))
# print(ord("B"))
# print(chr(65))
# print(ord("ก"))

def ascii_table(): # 0 - 255 (8-bit)
    for i in range(0, 256):
        print("{0} {0:c}".format(i))

# utf-8
def unicode_table(): #
    for i in range(ord("ก"), ord("ฮ") + 1):
        print("{0} {0:#x} {0:c}".format(i))

def unicode_table2():  #
    for i in range(0xe81, 0xea0):
        print("{0} {0:#x} {0:c}".format(i))


# ascii_table()

unicode_table2()