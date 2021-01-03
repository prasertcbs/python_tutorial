# https://en.wikibooks.org/wiki/Vehicle_Identification_Numbers_(VIN_codes)/Check_digit

def vin_checkdigit(vin):
    weight = (
        8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2
    )
    t = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 1, "K": 2,
        "L": 3, "M": 4, "N": 5, "P": 7, "R": 9, "S": 2, "T": 3, "U": 4, "V": 5, "W": 6,
        "X": 7, "Y": 8,
        "Z": 9, "_": 0
    }
    total = 0
    for v, w in zip(vin, weight):
        if v.isdigit():
            total += int(v) * w
        else:
            total += t[v.upper()] * w
    r = total % 11
    return "X" if r == 10 else str(r)

def vin_checkdigit2(vin):
    weight = (
        8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2
    )
    t = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 1, "K": 2,
        "L": 3, "M": 4, "N": 5, "P": 7, "R": 9, "S": 2, "T": 3, "U": 4, "V": 5, "W": 6,
        "X": 7, "Y": 8, "Z": 9, "_": 0, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9
    }
    total = 0
    for v, w in zip(vin, weight):
        total += t[v.upper()] * w
    r = total % 11
    return "X" if r == 10 else str(r)

def vin_checkdigit3(vin):
    weight = (
        8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2
    )
    t = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "J": 1, "K": 2,
        "L": 3, "M": 4, "N": 5, "P": 7, "R": 9, "S": 2, "T": 3, "U": 4, "V": 5, "W": 6,
        "X": 7, "Y": 8, "Z": 9, "_": 0, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9
    }
    r = sum([t[v.upper()] * w for v, w in zip(vin, weight)]) % 11
    return "X" if r == 10 else str(r)

# print(vin_checkdigit("1M8GDM9A_KP042788"))
# print(vin_checkdigit("LJCPCBLCX11000237"))
print(vin_checkdigit("JHLRD77874C026456"))
print(vin_checkdigit2("JHLRD77874C026456"))
print(vin_checkdigit3("JHLRD77874C026456"))


