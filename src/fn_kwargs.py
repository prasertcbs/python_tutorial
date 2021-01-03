def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["age"])

def full_name(**parts):
    d = []
    for k in ("first_name", "middle_name", "last_name"):
        if k in parts:
            # print(parts[k])
            d.append(parts[k])
    return " ".join(d)

f(name="Peter", age=21, hero="spiderman")
s = full_name(first_name="Peter", last_name="Parker")
print(s)
print("-" * 50)
t = full_name(first_name="George", middle_name="P", last_name="Wood")
print(t)
print("-" * 50)
u = full_name(first_name="Taylor")
print(u)
