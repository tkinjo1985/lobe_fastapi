from base64 import b64encode
from PIL import Image


def image2base64(filename):
    with open(filename, 'rb') as f:
        data = b64encode(f.read())

    return data


def resize_image(filename, width, height):
    image = Image.open(filename)
    resize_image = image.resize((width, height))
    resize_image.save(f'resized_{filename}')
