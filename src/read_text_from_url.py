import urllib.request


# https://dl.dropboxusercontent.com/u/23148470/planet.txt

def read_from_url(link):
    with urllib.request.urlopen(link) as f:
        s = f.read()
    # print(s)
    # print(type(s))
    # s1 = s.decode("utf8")
    # print(type(s1))
    # print(s1)
    return s.decode("utf8")


def read_from_url2(link):
    with urllib.request.urlopen(link) as f:
        for line in f:
            # print("- {}".format(line))
            print("- {}".format(line.decode("utf8")), end="")
            # print(s)
            # print(type(s))
            # s1 = s.decode("utf8")
            # print(type(s1))
            # print(s1)


t = read_from_url("https://dl.dropboxusercontent.com/u/23148470/planet.txt")
print("t = ", t)
lines = t.splitlines()
print("lines = ", lines)
# read_from_url2("https://dl.dropboxusercontent.com/u/23148470/planet.txt")
