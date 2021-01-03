import datetime
# ref: https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

def date_format_demo():
    d = datetime.date(2016,4,1)
    print(d.strftime("%d-%m-%y"))
    fmt = [
        "%d/%m/%y",
        "%a %d %b %Y",
        "%A %d %B %Y",
        "%d-%b-%y"
    ]
    for f in fmt:
        print("{:20} - > {}".format(f, d.strftime(f)))

def time_format_demo():
    d = datetime.datetime(2016,4,1,16,28,45)
    print(d)
    print(d.strftime("%d-%m-%y %H:%M:%S"))
    fmt = [
        "%d/%m/%y %H:%M",
        "%a %d %b %Y %I:%M%p"
    ]
    for f in fmt:
        print("{:20} - > {}".format(f, d.strftime(f)))

# date_format_demo()
time_format_demo()