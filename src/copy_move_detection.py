import cv2
import numpy as np

def detect_copy_move(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ORB detector
    orb = cv2.ORB_create(nfeatures=2000)

    kp, des = orb.detectAndCompute(gray, None)

    if des is None:
        return "Not Detected"

    # Match features
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des, des)

    # Filter matches (remove self matches)
    good_matches = []
    for m in matches:
        if m.distance < 30 and m.queryIdx != m.trainIdx:
            pt1 = kp[m.queryIdx].pt
            pt2 = kp[m.trainIdx].pt

            # Distance between points
            dist = np.linalg.norm(np.array(pt1) - np.array(pt2))

            if dist > 20:  # avoid nearby matches
                good_matches.append(m)

    # 🔥 KEY FIX: LOWER THRESHOLD
    if len(good_matches) > 15:
        return "Detected"
    else:
        return "Not Detected"