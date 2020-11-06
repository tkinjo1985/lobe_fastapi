Implementing an API with a combination of Lobe and FastAPI.
sample_model is predict cat or dog from image.

## SetUp
Run FastAPI Server form DockerImage
```
# docker-compose up --build -d
```
open http://localhost:8000/docs

if not use docker. need set up FastAPI Server.

[FastAPI WebPage](https://fastapi.tiangolo.com/)

## Prediction(Use sample_model)
predict from  base64 converted images.
```
import json
import requests
from image_utils import image2base64, resize_image

def predict_from_base64(image_base64, url):
    image_b64 = image_base64.decode('utf8')
    data = {'base64_str': image_b64}
    response = requests.post(url, data=json.dumps(data))
    label = json.loads(response.text)['label']

    return label

# if image size not (224, 224, 3) need resize.
# This function is save the risize image.
# ex… dog.9994.jpg -> resized.9994.jpg
resize_image('imagefile', 224, 224)

# convert image to base64.
image_bae64 = image2base64('sample_image/resize.dog.9994.jpg')

# endpoint for predict from base64
predict_url_base64 = 'http://localhost:8000/predict_from_base64/'

# send predict request
r = predict_from_base64(image_bae64, predict_url_base64)
```

if predict from images:
```
def predict_from_image(filename, url):
    files = [('file', open(filename, 'rb'))]
    response = requests.post(url, files=files)
    label = json.loads(response.text)['label']

    return label

# endpoint for predict from image
predict_url_image = 'http://localhost:8000/predict_from_image/'

# send predict request(not need resize image.)
r = predict_from_image('sample_image/dog.9994.jpg', predict_url_image) 
```

## For use your original model
changed model path(main.py)
```main.py
# create model instance
# model = ImageModel('model folder path')
model = ImageModel('sample_model')
```
