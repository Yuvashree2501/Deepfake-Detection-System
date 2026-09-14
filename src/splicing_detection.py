import cv2
import numpy as np

def detect_splicing(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur + difference method
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    diff = cv2.absdiff(gray, blur)

    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    ratio = np.sum(thresh > 0) / thresh.size

    if ratio > 0.01:
        return "Detected"
    else:
        return "Not Detected"