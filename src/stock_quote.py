import datetime
import urllib.request


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
        s = f.read()  # bytes sequence
    # print(s)
    # print(s.decode("utf8"))
    # with open("stock.csv", "w") as fw:
    #     fw.write(s.decode("utf8"))
    # with open("stock2.csv", "wb") as fw:
    #     fw.write(s)
    return s


q = get_stock_quote("aapl", "20160812", "20160905")
print(q.decode("utf8"))
