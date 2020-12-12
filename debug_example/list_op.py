def list_op():
    m=[]
    m.append('mocha')
    m.append('latte')
    a=m
    m.append('espresso')
    m[1]='green tea'
    del m[0]
    m.remove('espresso')
    print(f'm={m}')
    print(f'a={a}')

if __name__ == "__main__":
    list_op()
