def for_loop():
    total = 0
    for i in range(1, 6):
        total = total + i
    print(total)

def while_loop():
    i = 1
    while (i < 5):
        print(i)
        i += 1
    print(f'i={i}')

if __name__ == "__main__":
    for_loop()
    while_loop()
