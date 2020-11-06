import json
import requests
# from image_utils import image2base64, resize_image


def predict_from_image(filename, url):
    files = [('file', open(filename, 'rb'))]
    response = requests.post(url, files=files)
    label = json.loads(response.text)['label']

    return label


def predict_from_base64(image_base64, url):
    image_b64 = image_base64.decode('utf8')
    data = {'base64_str': image_b64}
    response = requests.post(url, data=json.dumps(data))
    label = json.loads(response.text)['label']

    return label
