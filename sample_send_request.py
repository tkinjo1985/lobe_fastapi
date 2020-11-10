from request_utils import predict_from_base64
from image_utils import preprocess_image

url = 'http://localhost:8000/predict_from_base64/'

image_base64 = preprocess_image('sample_image/dog.999.jpg', 224, 224)
label = predict_from_base64(image_base64, url)
print(label)
