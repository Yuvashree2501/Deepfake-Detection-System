
import os
import cv2
import numpy as np

from keras.models import load_model

from copy_move_detection import detect_copy_move
from splicing_detection import detect_splicing


# ---------------------------------
# MODEL PATH
# ---------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "../models/deepfake_model.h5")

# Load trained model
model = load_model(MODEL_PATH)


# ---------------------------------
# IMAGE PREPROCESSING
# ---------------------------------

def preprocess_image(image_path):

    img = cv2.imread(image_path)

    img = cv2.resize(img, (224, 224))

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    return img


# ---------------------------------
# MAIN ANALYSIS FUNCTION
# ---------------------------------

def analyze_image(image_path):

    # ---------------------------------
    # AI DETECTION
    # ---------------------------------

    processed_img = preprocess_image(image_path)

    prediction = model.predict(processed_img)[0][0]

    ai_score = float(prediction)

    print("RAW MODEL PREDICTION:", ai_score)

    # ---------------------------------
    # MODEL LOGIC
    # fake = LOW VALUE
    # real = HIGH VALUE
    # ---------------------------------

    fake_probability = (1 - ai_score) * 100

    # ---------------------------------
    # AI GENERATED RESULT
    # ---------------------------------

    if fake_probability > 75:
        ai_generated = "Yes"

    elif fake_probability > 45:
        ai_generated = "Uncertain"

    else:
        ai_generated = "No"

    # ---------------------------------
    # COPY-MOVE DETECTION
    # ---------------------------------

    try:
        copy_move = detect_copy_move(image_path)

    except Exception as e:
        print("Copy-Move Error:", e)
        copy_move = "Not Detected"

    # ---------------------------------
    # SPLICING DETECTION
    # ---------------------------------

    try:
        splicing = detect_splicing(image_path)

    except Exception as e:
        print("Splicing Error:", e)
        splicing = "Not Detected"

    # ---------------------------------
    # FINAL RISK SCORE
    # ---------------------------------

    risk_score = fake_probability

    # Small forensic contribution
    if copy_move == "Detected":
        risk_score += 3

    if splicing == "Detected":
        risk_score += 3

    # Prevent automatic 100%
    if risk_score > 95:
        risk_score = 95

    risk_score = round(risk_score, 2)

    # ---------------------------------
    # FINAL RESULT
    # ---------------------------------

    if risk_score < 35:
        final_result = "Authentic"

    elif risk_score < 75:
        final_result = "Suspicious"

    else:
        final_result = "Fake"

    # ---------------------------------
    # RETURN RESULTS
    # ---------------------------------

    return {

        "ai_generated": ai_generated,

        "copy_move": copy_move,

        "splicing": splicing,

        "risk_score": risk_score,

        "final_result": final_result
    }

