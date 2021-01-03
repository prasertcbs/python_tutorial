def temperature_table():
    for celsius in range(101): # 0 - 100
        f = (celsius * 9 / 5) + 32
        # print(celsius, " = ", f)
        print("{}C = {:.2f}F".format(celsius, f))

def mult_table(from_n, to_n):
    # nested loop
    for i in range(from_n, to_n + 1):
        for j in range(1, 13): # nested loop
            print("{} x {} = {}".format(i, j, i * j))
        print("-" * 40)

temperature_table()
mult_table(2,3)