import json
import os

import tensorflow as tf


class ImageModel:
    def __init__(self, model_path):
        """
        modelを読み込みます。

        paramter:
        model_paht: modelの保存パス
        """
        try:
            self.model = tf.saved_model.load(model_path)
            self.infer = self.model.signatures['serving_default']
        except OSError as err:
            print('modelが見つかりません。modelの保存先と名前を確認してください。')
            print(err)

    def get_input_shape(self, signature_path):
        """
        signature(署名)からmodelへのinput_shapeを取得します。

        parameter:
        signature: signatureファイル(signature.json)

        return:
        input shape:　modelへの入力サイズ
        """
        if os.path.exists(signature_path):
            with open(signature_path, 'r') as f:
                signature = json.load(f)
            inputs = signature.get('inputs')
            return inputs['Image']['shape'][1:]
        else:
            print('signatureファイルが見つかりません。')

    def predict(self, image):
        """
        与えられた画像から正解ラベルを予測します。

        Parameter:
        image: 予測したい画像(numpy.ndarray)

        Return:
        predict: 予測結果
        """
        predict = self.infer(tf.constant(image))['Prediction'][0]
        return predict.numpy().decode()
