# import random
#
# for _ in range(5):
#     print("hello")
#
# for _ in range(5):
#     print(random.randint(1, 6))

__all__ = ["circle", "Alpha", "_Beta", "_rectangle"]
_recipe = "a7b3c15" # private
vat = .07

def _rectangle(w, h):
    return w*h

def circle(r):
    return 22 / 7 * r * r

class Alpha:
    @staticmethod
    def foo():
        print("hello")

class _Beta:
    @staticmethod
    def bar():
        print("wow")



