def var_scope():
    a = 'Peter'
    b = 'Parker'
    c = a + ' ' + b
    print(c)


if __name__ == "__main__":
    a = 5
    b = 7
    c = a*b
    var_scope()
    print(a, b, c)
    a=['one', 'two']
    a.append('mocha')
    a.remove('two')