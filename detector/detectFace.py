import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras


def resize_image(image):
    smaller = cv2.resize(image, (224, 224))
    return smaller


def detect_face_in_image(image):
    image_cp = image.copy()
    smaller_img = resize_image(image_cp)
    image_shape = smaller_img.shape

    print('Resized Shape:  ', image_shape)

    model = tf.keras.applications.ResNet50(weights='imagenet')

    image_4d = np.expand_dims(smaller_img, 0)
    print(image_4d.shape)
    predictions = model.predict(image_4d, verbose=3)
    decoded = keras.applications.resnet50.decode_predictions(predictions, top=3)

    print(predictions.shape)

    print(decoded)
    print(decoded[0][0])

    return image_cp, decoded
