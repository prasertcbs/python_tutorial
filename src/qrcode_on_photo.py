# %%
# pip install Pillow qrcode
import qrcode  # https://pypi.python.org/pypi/qrcode
from PIL import Image, ImageFont, ImageDraw

# %%
def create_qrcode(text, box_size=10, border=1):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=box_size,  # multiple of 25
        border=border  # multiple of 20
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def add_watermark(base_img, watermark_img, posx=0, posy=0):
    tmp_img = base_img.copy()
    tmp_img.paste(watermark_img, (posx, posy))
    # tmp_img.show()
    # tmp_image.save(output_image_path)
    return tmp_img


def single(input_img_filename, qr_text, output_img_filename):
    qr_img = create_qrcode(qr_text, box_size=6, border=1)
    base_img = Image.open(input_img_filename)
    new_img = add_watermark(base_img, qr_img, base_img.size[0] - qr_img.size[0],
                            base_img.size[1] - qr_img.size[1])
    # new_img.show()
    new_img.save(output_img_filename)


def batch():
    product_info = ['little sheep', 'coffee bean', 'nan จังหวัดน่าน', 'jam']
    for i in range(1, 5):
        qr_img = create_qrcode(product_info[i - 1], box_size=6, border=1)
        s = f'photo-{i}.jpg'
        base_img = Image.open(s)
        new_img = add_watermark(base_img, qr_img, 0,
                                base_img.size[1] - qr_img.size[1])
        # new_img = add_watermark(base_img, qr_img, base_img.size[0] - qr_img.size[0],
        #                         base_img.size[1] - qr_img.size[1])
        # new_img.show()
        new_img.save(f'qr2-{s}')

# %%
if __name__ == '__main__':
    # create_qrcode("Beautiful day").show()
    # create_qrcode("Beautiful day").save("qr_beautiful.png")
    # single("photo-1.jpg", "little sheep\nline: @abc", "qr_sheep.jpg")
    batch()

