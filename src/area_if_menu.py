def rectangle(w, h): # dynamic typing
    # code block
    area = w * h
    return area

def triangle(w, h):
    # area = .5 * w * h
    return .5 * w * h


# main entry point
print("1. rectangle")
print("2. triangle คำนวณพื้นที่สามเหลี่ยม")
n = input("please select option: ")
w = int(input("width = ")) # string '5' "5"
h = int(input("height = ")) # "3"
if n == "1":
    print("rectangle area")
    print(rectangle(w, h))
else:
    print("triangle area")
    print(triangle(w,h))
