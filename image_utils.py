from base64 import b64encode
from PIL import Image
import os


def image2base64(filename):

    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            data = b64encode(f.read())
        return data
    else:
        print('Image Not Found')


def resize_image(filename, width, height):

    if os.path.exists(filename):
        image = Image.open(filename)
        resize_image = image.resize((width, height))
        resize_image.save(f'resized_{filename}')
    else:
        print('Image Not Found')
