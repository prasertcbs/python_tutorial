import datetime
import urllib.request
import sys


def get_stock_quote(stock, from_yyyymmdd, to_yyyymmdd):
    # http://chart.finance.yahoo.com/table.csv?s=MSFT&a=8&b=6&c=2016&d=8&e=11&f=2016&g=d&ignore=.csv
    fdate = datetime.datetime.strptime(from_yyyymmdd, "%Y%m%d")
    tdate = datetime.datetime.strptime(to_yyyymmdd, "%Y%m%d")
    param = "s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d&ignore=.csv".format(
        stock, fdate.month - 1, fdate.day, fdate.year,
               tdate.month - 1, tdate.day, tdate.year
    )
    link = "http://chart.finance.yahoo.com/table.csv?" + param
    with urllib.request.urlopen(link) as f:
        s = []
        for i, line in enumerate(f):
            if i == 0:
                s.append("{},{}".format("stock", line.decode("utf8")))
            else:
                s.append("{},{}".format(stock, line.decode("utf8")))
    return "".join(s)


def write_stock_csv(filename, data):
    with open(filename, "w") as f:
        f.write(data)


# q = get_stock_quote("scc.bk", "20160801", "20160831")
q = get_stock_quote(sys.argv[1], sys.argv[2], sys.argv[3])
print(q)

# for i, arg in enumerate(sys.argv):
#     print(i, arg)

# symbols = ["scc.bk", "bbl.bk", "bh.bk"]
# for symbol in symbols:
#     q = get_stock_quote(symbol, "20160812", "20160905")
#     write_stock_csv(symbol + ".csv", q)
