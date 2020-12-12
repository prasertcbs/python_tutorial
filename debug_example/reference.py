# pass by value vs. reference
# use Python Preview to monitor variables

def process1(items, customer_name, amount):
    customer_name = 'Peter Parker'
    amount = amount * .8
    for s in items:
        s = s.upper()


def process2(items, customer_name, amount):
    customer_name = 'Peter Parker'
    amount = amount * .8
    for i in range(len(items)):
        items[i] = items[i].upper()


def process3(items, customer_name, amount):
    customer_name = 'Peter Parker'
    amount = amount * .8
    items.append('americano')


def process4(items, customer_name, amount):
    customer_name = 'Peter Parker'
    amount = amount * .8
    new_items = items
    new_items.append('americano')


def process5(items, customer_name, amount):
    customer_name = 'Peter Parker'
    amount = amount * .8
    new_items = items.copy()
    new_items.append('americano')


if __name__ == "__main__":
    menus = ['mocha', 'latte', 'espresso']
    customer_name = 'Peter'
    amount = 120
    process4(menus, customer_name, amount)
    print(menus, customer_name, amount)
