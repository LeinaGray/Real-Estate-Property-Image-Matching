from tensorflow.keras import Model
from tensorflow.keras.applications import MobileNetV3Large
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam


trainPath = "dataset/ai_image_detection/train_dataset"
testPath = "dataset/ai_image_detection/test_dataset"


trainGenerator = ImageDataGenerator(
    rotation_range = 15, 
    width_shift_range = 0.1,
    height_shift_range = 0.1, 
    brightness_range = (0, 0.2)).flow_from_directory(
        trainPath, 
        target_size = (320, 320), 
        batch_size = 32)

testGenerator = ImageDataGenerator(
    rotation_range = 15, 
    width_shift_range = 0.1,
    height_shift_range = 0.1, 
    brightness_range = (0, 0.2)).flow_from_directory(
        testPath, 
        target_size = (320, 320), 
        batch_size = 32)

# Build the model

baseModel = MobileNetV3Large(weights = "imagenet", include_top = False)
x = baseModel.output

# Add 5 layers to the model
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(128, activation='relu')(x)
predictionLayer = Dense(2, activation='softmax')(x)


model = Model(inputs = baseModel.input, outputs = predictionLayer)
print(model.summary())

# freeze the layers of the MobileNetV3 (already trained)

for layer in model.layers[:-5]:
    layer.trainable = False

# Compile

optimizer = Adam(learning_rate = 0.0001)
model.compile(loss = "categorical_crossentropy", optimizer = optimizer, metrics = ['accuracy'])

# train
model.fit(trainGenerator, validation_data = testGenerator, epochs = 5)

modelSavedPath  = "fraud-filter-system/ai-image-detection/AI-detector-model-Mnet-V3.h5"
model.save(modelSavedPath)

# Results
# - accuracy: 0.9614 - loss: 0.0920 - val_accuracy: 0.9683 - val_loss: 0.0799 