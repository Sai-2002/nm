import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input


label_mapping = {
    0: 'Anthracnose',
    1: 'Algal Leaf',
    2: 'Bird Eye Spot',
    3: 'Brown Blight',
    4: 'Gray Light',
    5: 'Healthy',
    6: 'Red Leaf Spot',
    7: 'White Spot',
    
} 

def givePredict(filename):

    model = load_model('./model.h5')

    image = load_img(f'./static/uploads/{filename}', target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)

    yhat = model.predict(image)
    print(yhat)

    top_prediction_index = np.argmax(yhat)

    predicted_label = label_mapping[top_prediction_index]

    print("Predicted label:", predicted_label)

    return predicted_label

