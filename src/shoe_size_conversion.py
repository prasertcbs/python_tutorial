
def conversion(size, from_unit, to_unit):
    # women's shoe size
    d = {
        "US": [4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12],
        "UK": [2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10],
        "CM": [20.8,21.3,21.6,22.2,22.5,23,23.5,23.8,24.1,24.6,25.1,25.4,25.9,26.2,26.7,27.1,27.6]
    }
    d1 = d[from_unit]
    d2 = d[to_unit]
    to_size = d2[d1.index(size)]
    print("{} {} = {} {}".format(size, from_unit, to_size, to_unit))


if __name__ == '__main__':
    # size = float(input("size: "))
    # from_unit = input("US/UK/CM: ")
    # to_unit = input("US/UK/CM: ")
    s = input("7 uk cm: ")
    size, from_unit, to_unit = s.strip().upper().split(" ")
    conversion(float(size), from_unit, to_unit)
