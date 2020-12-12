def dictionary():
    d = {"sun": "red",
         "mon": "yellow",
         "tue": "pink",
         "wed": "green",
         "thu": "orange",
         "fri": "blue",
         "sat": "purple"}
    for k, v in d.items():
        print(k, v)
    print(d['wed'])


def menu():
    m = [{"name": "burger", "price": 99},
         {"name": "coke", "price": 30}
         ]
    print(m[0]['name'])


# dictionary()
menu()