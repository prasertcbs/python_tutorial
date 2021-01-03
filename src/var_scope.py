x = "Peter Parker"    # global scope / module scope
nums = [4, 7, 8]
def fn():
    x = "Spiderman" # local
    print(nums)
    print("inside fn()", x)

def fn2():
    x = "Mr. "  + x
    print("inside fn()", x)

def fn3():
    global x
    x = "Mr. "  + x
    print("inside fn()", x)

print(x)
fn()
# fn3()
print(x)
