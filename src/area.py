def rectangle(w, h): # dynamic typing
    # code block
    area = w * h
    return area

def triangle(w, h):
    # area = .5 * w * h
    return .5 * w * h


# main entry point
w = int(input("width = ")) # string '5' "5"
h = int(input("height = ")) # "3"
# print(rectangle(w, h))
print(triangle(w,h))