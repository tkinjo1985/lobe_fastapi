import os
from base64 import b64encode
import base64
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from PIL import Image
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
def predict(file: UploadFile = File(...)):
    filepath = save_upload_file_tmp(file)
    image = Image.open(filepath)
    image = image.resize((input_shape[0], input_shape[1]))
    image = np.array(image, dtype=np.float32) / 255.0
    image = image.reshape(
        [1, input_shape[0], input_shape[1], input_shape[2]])
    label = model.predict(image)
    return {'label': label}


@app.post("/predict_from_base64/")
def predict_from_base64(image: ImageBase64):
    image_base64 = image.base64_str
    image_dec = base64.b64decode(image_base64)
    image_np = np.frombuffer(image_dec, dtype='uint8')
    decimg = cv2.imdecode(image_np, 1).astype(np.float32) / 225.0
    image_predict = decimg.reshape(
        [1, input_shape[0], input_shape[1], input_shape[2]])
    label = model.predict(image_predict)
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
