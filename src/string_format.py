def demo():
    first_name = "peter"
    last_name = "parker"
    age = 21

    print(first_name, last_name, age)
    print("{} {} age: {}".format(first_name, last_name, age))
    print("{0} {1} age: {2}".format(first_name, last_name, age))
    print("{1}, {0} age: {2}".format(first_name, last_name, age))  # position

def demo_number():
    # n = 1218123000
    # print("{}".format(n))
    # print("{:,}".format(n))

    d = 234322.756321
    a = -1234.50
    b = -343.25
    # print("{}".format(d))
    # print("{:.2f}".format(d))
    print("{:,.2f}".format(d))
    print("{:,.2f}".format(a))
    print("{:,.2f}".format(b))

    print("-" * 50)
    print("{:15,.2f}".format(d))    # align right
    print("{:=15,.2f}".format(a))
    print("{:15,.2f}".format(b))

demo_number()