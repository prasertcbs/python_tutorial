import webbrowser
from urllib.request import urlopen


def read_image_url(url, output_image_file):
    with urlopen(url) as response, open(output_image_file, "wb") as out_file:
        data = response.read()
        out_file.write(data)

def read_index(symbols):
    for s in symbols:
        url = "http://www.reuters.wallst.com/enhancements/chartapi/index_chart_api.asp?symbol={}&headerType=quote&width=540&height=249&duration=5".format(s)
        output_image_file = s[1:] + ".png"
        read_image_url(url, output_image_file)

if __name__ == '__main__':
    # url = "https://images-na.ssl-images-amazon.com/images/I/71%2BtFOBFWZL._SL1500_.jpg"
    # url = "http://www.reuters.wallst.com/enhancements/chartapi/index_chart_api.asp?symbol=.DJI&headerType=quote&width=540&height=249&duration=5"
    # # webbrowser.open(url)
    # read_image_url(url, "demo.jpg")

    symbols = (".DJI", ".N225", ".GDAXI")
    read_index(symbols)