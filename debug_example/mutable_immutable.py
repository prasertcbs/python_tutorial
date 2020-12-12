# understanding mutable vs immutable
menus=['mocha', 'latte', 'espresso', 'green tea']
menus[0]='iced mocha'
menus.sort()

for m in menus:
    s=m
    print(s)

    
flowers=('rose', 'tulip', 'lily')
flowers=('jasmine', 'tulip', 'lily')

# menus.append('americano')
# flowers[0]='jasmine' # tuple is immutable

items=list(flowers)

