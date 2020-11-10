import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import sys
import pathlib
import pickle
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
from tensorflow import keras


batch_size = 7
img_height = 1600
img_width = 1200


class_names = pickle.loads(open('labels.pickle', "rb").read()) # Load the class names
model = tf.keras.models.load_model('saved_model/exercise_model')

def predictFiles(File):
### Prediction ###
# Knee
    print(File)
    sunflower_path = File

    img = keras.preprocessing.image.load_img(
        sunflower_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    #sunflower_path = "./testData/squat/AoMJn.png"

    #img = keras.preprocessing.image.load_img(
    #    sunflower_path, target_size=(img_height, img_width)
    #)
    #img_array = keras.preprocessing.image.img_to_array(img)
    #img_array = tf.expand_dims(img_array, 0) # Create a batch

    #predictions = model.predict(img_array)
    #score = tf.nn.softmax(predictions[0])

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            for filename in os.listdir(arg):
                if filename.endswith("png"):
                    predictFiles(os.path.join(arg, filename))
                else:
                    continue