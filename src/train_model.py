import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# ==============================
# DATASET PATH
# ==============================
dataset_path = r"C:\Users\yuva0\Desktop\Deepfake-Detection-System\dataset"

# ==============================
# DATA GENERATOR
# ==============================
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

print("Class Mapping:", train_data.class_indices)

# ==============================
# LOAD MOBILENETV2
# ==============================
base_model = MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights='imagenet'
)

# Freeze base model
base_model.trainable = False

# ==============================
# ADD CLASSIFIER
# ==============================
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ==============================
# TRAIN
# ==============================
print("🚀 Training started...")
model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# ==============================
# SAVE MODEL
# ==============================
os.makedirs("../models", exist_ok=True)
model.save("../models/deepfake_model.h5")

print("✅ MobileNetV2 model saved!")