
import json
import requests


def predict_from_image(filename, url):
    files = [('file', open(filename, 'rb'))]
    response = requests.post(url, files=files)
    label = json.loads(response.text)['label']

    return label


def predict_from_base64(image_base64, url):
    data = {'base64_str': image_base64}
    response = requests.post(url, data=json.dumps(data))
    label = json.loads(response.text)['label']

    return label
