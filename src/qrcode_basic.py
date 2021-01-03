# %%
# pip install Pillow qrcode
import qrcode  # https://pypi.python.org/pypi/qrcode


def basic():
    # txt = "hello QRCode"
    txt = '''
    line: @myline
    fb: @myfacebook
    m: 0891234321
    '''
    img = qrcode.make(txt)
    img.show()


def adv():
    qr = qrcode.QRCode(box_size=5, border=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L)  # box_size x 25
    qr.add_data("https://youtube.com/prasertcbs")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    # img.save("qr5.png")

# %%
if __name__ == '__main__':
    # basic()
    adv()


# %%
