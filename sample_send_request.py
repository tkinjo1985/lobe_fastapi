from request_utils import predict_from_base64, predict_from_image
from image_utils import image2base64

# url = 'http://localhost:8000/predict_from_base64/'
url = 'http://localhost:8000/predict_from_image/'

# image_base64 = image2base64('sample_image/dog.999.jpg')
# label = predict_from_base64(image_base64, url)
label = predict_from_image('sample_image/dog.9994.jpg', url)
print(label)
