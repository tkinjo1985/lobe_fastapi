from base64 import b64encode
from PIL import Image
import os
from io import BytesIO


def image_resize(filename, width, height):

    if os.path.exists(filename):
        image = Image.open(filename)
        if image.size == (width, height):
            return image
        resized_image = image.resize((width, height))
        return resized_image
    else:
        print('Image Not Found')


def image2base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_b64 = b64encode(buffered.getvalue())
    return img_b64.decode('utf8')


def preprocess_image(filename, width, height):
    image = image_resize(filename, width, height)
    image_base64 = image2base64(image)
    return image_base64
