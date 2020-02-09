import numpy as np
from keras.applications.vgg16 import (
    VGG16, preprocess_input, decode_predictions)

from keras.preprocessing import image

def load_image(path):
    img_path = path
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x
img = load_image('./images/cat.jpeg')
model = VGG16(weights='imagenet')
predictions = model.predict(img)
# convert the probabilities to class labels
label = decode_predictions(predictions)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))
# print(np.argmax(predictions))