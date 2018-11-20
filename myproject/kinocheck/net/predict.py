import os
import sys
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img, img_to_array
from keras import backend as K

def predict(target):
    classes = ["食用キノコの可能性が高いです！","毒キノコの可能性が高いです、非常に危険です！"]
    K.clear_session()
    img_width, img_height = 200, 150
    result_dir = "results"
    uploads_dir = "./uploads/"
    model_name = "kinocheck.h5"
    #graph = tf.get_default_graph()
    #global graph
    #with graph.as_default():

    test_datagen = ImageDataGenerator(rescale=1.0 / 255)
    model = load_model(os.path.join(result_dir, model_name))

    test_X = load_img(os.path.join(uploads_dir, target), target_size=(img_height, img_width))
    test_X = img_to_array(test_X)
    test_X = np.expand_dims(test_X, axis=0)
    test_X /= 255.
    test_y = model.predict(test_X, steps=1)
    return classes[np.argmax(test_y)]
