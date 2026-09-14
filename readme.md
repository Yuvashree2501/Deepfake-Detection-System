\# Deepfake Detection System



An AI-powered image forensics web application that analyzes images for AI-generated content and common image manipulation.



\## Overview



The Deepfake Detection System is a Flask-based web application designed to analyze uploaded images using a trained deep learning model along with copy-move and splicing detection techniques.



The system generates an analysis report containing:



\- AI-generated image detection

\- Copy-move detection

\- Splicing detection

\- Risk score

\- Final classification



\## Features



\### AI-Generated Image Detection

Uses a trained deep learning model to analyze an uploaded image and estimate the probability that the image is AI-generated.



\### Copy-Move Detection

Analyzes the image for possible copy-move manipulation.



\### Splicing Detection

Analyzes the image for possible splicing manipulation.



\### Risk Score

Combines the AI detection result with detected forensic indicators to generate a risk score.



\### Final Classification

The image is classified as:



\- Authentic

\- Suspicious

\- Fake



\## Technologies Used



\- Python

\- Flask

\- TensorFlow / Keras

\- OpenCV

\- NumPy

\- Pillow

\- Scikit-image

\- Scikit-learn

\- Matplotlib

\- HTML

\- CSS



\## System Workflow



```text

Upload Image

&nbsp;    ↓

Image Preprocessing

&nbsp;    ↓

AI-Generated Detection

&nbsp;    ↓

Copy-Move Detection

&nbsp;    ↓

Splicing Detection

&nbsp;    ↓

Risk Score Calculation

&nbsp;    ↓

Final Classification

&nbsp;    ↓

Analysis Report

