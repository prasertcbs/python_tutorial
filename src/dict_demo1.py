def demo():
    d = {"hello": "สวัสดี", "thank you": "ขอบคุณ", "toilet": "ห้องน้ำ"}
    print(d["hello"])
    d["one"] = "หนึ่ง"
    print(d)
    del d["toilet"]
    print(d)

def demo2():
    m = {"th": [5, 3, 7],
         "sg": [3, 1, 2]}
    print(m)
    print(m["th"])
    print(m["th"][0])
    print(m["th"][0]+m["th"][1]+m["th"][2])

# demo()
demo2()