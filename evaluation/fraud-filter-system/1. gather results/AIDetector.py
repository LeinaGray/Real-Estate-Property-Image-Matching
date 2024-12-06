import os
from tensorflow import image
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.utils import img_to_array



# folder_path = r"dataset\training-dataset\AI\train_dataset"
# categories = os.listdir(folder_path)
# categories.sort()
# print(categories)

categories = ['AI Images', 'Authentic Images']

# load the saved model
modelSavedPath = r"C:\Users\lenovo\OneDrive\Documents\PROJECTS\ALT\Real-Estate-Image-Matching\models\AI-detection-model.keras"
model = tf.keras.models.load_model(modelSavedPath)

# predict the image
def classify_image(imageFile):
    x = []
    img = Image.open(imageFile).convert('RGB')
    img.load()
    img = img.resize((320, 320), Image.LANCZOS)

    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Add a new dimension for batch size
    x = tf.convert_to_tensor(x)  # Convert to a tensor
    # print(x.shape)
    pred = model.predict(x)
    # print(pred)
    # Get the class probabilities
    class_probabilities = pred.squeeze()  # Remove extra dimensions

    # Print probabilities for both classes
    ai_probability = class_probabilities[0] * 100  # Assuming "AI Images" is at index 0
    authentic_probability = class_probabilities[1] * 100  # Assuming "Authentic Images" is at index 1

    print(f"AI Image: {ai_probability:.2f}%")
    print(f"Authentic Image: {authentic_probability:.2f}%")

    # get the highest prediction value
    categoryValue = np.argmax(pred, axis=1)
    categoryValue = categoryValue[0]

    print(categoryValue)

    result = categories[categoryValue]
    return result, ai_probability, authentic_probability

# AI_path = r"dataset\evaluation-dataset\AI\b1.jpg"
# authentic_path = r"dataset\evaluation-dataset\authentic\listing_897_image_7.png_20240927_170342.png"
# result, ai, authentic = classify_image(authentic_path)
# result, ai, authentic = classify_image(AI_path)
# print(result)
