# dunder -> double underscore

class Alpha:
    normal = 1
    _lucky = 13
    __secret = 777 # name mangled -> change _classname__attri

    def fx(self):
        print("this is fx in A")
    def _fy(self):
        print("this is fy in A")
    def __fz(self): # final method
        print("this is fz in A")

class Beta(Alpha):
    def __init__(self):
        self.greeting = "hello from beta"
    def __foo__(self):
        pass
    def __fz(self):
        print("THIS IS fz in B")

class __Gamma():
    def bar(self):
        print("hello from Gamma")

if __name__ == '__main__':
    # print(Alpha.normal)
    # print(Alpha._lucky)
    # print(Alpha.__secret)
    # print(Alpha._Alpha__secret)
    # print(Alpha.__dict__)
    # Alpha.normal = 99
    # Alpha._lucky = 123
    # Alpha.__secret = 9999
    # print(Alpha.normal)
    # print(Alpha._lucky)
    # print(Alpha.__secret)
    # print(Alpha._Alpha__secret)
    print(Alpha.__dict__)

    a=Alpha()
    a.fx()
    a._fy()
    # a.__fz()
    a._Alpha__fz()

    b = Beta()
    b._Beta__fz()
    b._Alpha__fz()

    g = __Gamma()
    g.bar()