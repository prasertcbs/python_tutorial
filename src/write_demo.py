def write_demo():
    f = open(r"demo_thai.txt", "w", encoding="utf8")
    f.write("HELLO python\n")
    f.write("I love ไพธอน.\n")
    f.write("line 3\n")
    f.close()


def write_context_mgr():
    with open(r"demo_thai2.txt", "w", encoding="utf8") as f:
        f.write("HELLO python\n")
        f.write("I love ไพธอน.\n")
        f.write("line 3\n")


def write_list():
    menu = ["mocha", "latte", "espresso"]
    with open("menu.txt", "w", encoding="utf8") as f:
        for m in menu:
            # f.write(m + "\n")
            f.write("{}\n".format(m.capitalize()))


# write_demo()
# write_context_mgr()
write_list()
