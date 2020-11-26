
from base64 import b64encode
from io import BytesIO

from PIL import Image


def image2base64(image_file):
    try:
        image = Image.open(image_file).convert('RGB')
    except Exception as err:
        print(err)
    else:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = b64encode(buffered.getvalue())
        return img_b64.decode('utf8')
