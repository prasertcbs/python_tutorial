# ==, <>, !=, <, >, <=, >=, not, and, or

# score = 65
# if score > 70:
#     print("good")
# else:
#     print("try harder")

def greeting(lang):
    if lang == "th":
        print("sawadee")
    else:
        print("hello")

def greeting2(lang):
    if lang == "th":
        print("sawadee")
        print("สวัสดี")
    elif lang == "jp":
        print("konichiwa")
    elif lang == "kr":
        print("ann-yeong")
    else:
        print("hello")

def meet_req(eng, interview):
    if eng > 70 and interview > 80:
        return True
    else:
        return False

def meet_req2(eng, interview, math):
    if eng > 70 and interview > 80 and math > 65:
        return True
    else:
        return False

# # greeting("aa")
# # greeting2("th")
# # print(meet_req(80, 90))
# # print(meet_req(80, 60))
# print(meet_req2(80, 90, 70))