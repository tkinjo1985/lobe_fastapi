import shutil
from base64 import b64decode
from pathlib import Path
from tempfile import NamedTemporaryFile

import cv2
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from model import ImageModel

# create FastAPI instance
app = FastAPI()


# create model instance
# model = ImageModel('model folder path')
model = ImageModel('sample_model')


class ImageBase64(BaseModel):
    base64_str: str


# get input shape for model from signature
input_shape = model.get_input_shape('sample_model/signature.json')


@app.post("/predict_from_image/")
async def predict(file: UploadFile = File(...)):
    filepath = save_upload_file_tmp(file)
    image = tf.keras.preprocessing.image.load_img(
        filepath, color_mode='rgb', target_size=(input_shape[0], input_shape[1]))
    image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
    image = tf.expand_dims(image, axis=0)
    label = model.predict(image)
    return {'label': label}


@app.post("/predict_from_base64/")
async def predict_from_base64(image: ImageBase64):
    image_base64 = image.base64_str
    image_np = np.frombuffer(b64decode(image_base64), dtype='uint8')
    decimg = cv2.imdecode(image_np, 1).astype(np.float32) / 225.0
    image = tf.expand_dims(decimg, axis=0)
    label = model.predict(image)
    return {'label': label}


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
        tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path
