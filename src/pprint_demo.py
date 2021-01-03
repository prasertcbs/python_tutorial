# pretty print
from pprint import pprint


nato = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

aqi_tbl = [
    [0, 'good', 'green'],
    [51, 'moderate', 'yellow'],
    [101, 'unhealthy for sensitive groups', 'orange'],
    [151, 'unhealthy', 'red'],
    [201, 'very unhealthy', 'purple'],
    [301, 'hazardous', 'maroon']
]

names = [
    {'name': 'Peter', 'score': 5},
    {'name': 'Jenny', 'score': 8},
    {'name': 'Bruce', 'score': 7},
    {'name': 'Ben', 'score': 10}]

menus = {
    "Mocha": {"S": 20, "M": 25, "L": 30},
    "Latte": {"S": 30, "M": 45, "L": 50},
    "Espresso": {"S": 35, "M": 40, "L": 45},
}

if __name__ == "__main__":
    # pprint(nato)
    # print(aqi_tbl)
    # print('-' * 80)
    # pprint(aqi_tbl)
    # print(names)
    # print('-' * 80)
    # pprint(names)
    print(menus)
    print('-' * 80)
    pprint(menus)