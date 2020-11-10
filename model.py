import json
import os

import tensorflow as tf


class ImageModel:
    def __init__(self, model_path):
        """
        Load a model.

        paramter:
        model_paht: model path
        """
        try:
            self.model = tf.saved_model.load(model_path)
            self.infer = self.model.signatures['serving_default']
        except OSError as err:
            print('model not found. check model name and path.')
            print(err)

    def get_input_shape(self, signature_path):
        """
        Load input shape to model from signature.

        parameter:
        signature: signature.json

        return:
        input shape:　input shape to model.
        """
        if os.path.exists(signature_path):
            with open(signature_path, 'r') as f:
                signature = json.load(f)
            inputs = signature.get('inputs')
            return inputs['Image']['shape'][1:]
        else:
            print('signature.json not found.')

    def predict(self, image):
        """
        Predict label from image.

        Parameter:
        image: numpy.ndarray

        Return:
        predict: label
        """
        predict = self.infer(tf.constant(image))['Prediction'][0]
        return predict.numpy().decode()
