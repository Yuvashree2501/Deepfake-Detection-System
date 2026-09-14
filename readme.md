# 🔍 Deepfake Detection System

### AI-Powered Image Forensics and Manipulation Detection

An AI-powered image forensics web application built with **Python, Flask, TensorFlow/Keras, and OpenCV** to analyze images for AI-generated content and common image manipulation techniques.

The system combines **deep learning-based detection** with **copy-move and splicing analysis** to generate an overall **risk score and final classification**.

---

## 📌 Overview

The **Deepfake Detection System** is designed to help analyze the authenticity of digital images.

Users can upload an image through the web interface, after which the system performs multiple levels of analysis:

- 🤖 AI-generated image detection
- 🔄 Copy-move manipulation detection
- ✂️ Image splicing detection
- 📊 Risk score calculation
- 🏷️ Final image classification

The final analysis is presented through a simple Flask-based web interface.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 AI-Generated Detection | Uses a trained deep learning model to analyze whether an image may be AI-generated |
| 🔄 Copy-Move Detection | Identifies possible duplicated regions within an image |
| ✂️ Splicing Detection | Analyzes images for possible splicing/manipulation |
| 📊 Risk Score | Calculates an overall image manipulation risk score |
| 🏷️ Final Classification | Classifies the image as Authentic, Suspicious, or Fake |
| 🌐 Web Interface | Provides an easy-to-use Flask-based image upload and analysis interface |

---

## 🧠 How It Works

The system follows a multi-stage image analysis process:

```text
                    ┌─────────────────┐
                    │   Upload Image  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Image           │
                    │ Preprocessing   │
                    └────────┬────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
     ┌──────────────────┐         ┌──────────────────┐
     │ AI-Generated     │         │ Image Forensics  │
     │ Detection        │         │ Analysis         │
     └────────┬─────────┘         └────────┬─────────┘
              │                            │
              │                    ┌───────┴────────┐
              │                    ↓                ↓
              │             Copy-Move          Splicing
              │             Detection          Detection
              │                    │                │
              └────────────────────┴────────────────┘
                                   ↓
                         ┌──────────────────┐
                         │  Risk Score      │
                         │  Calculation     │
                         └────────┬─────────┘
                                  ↓
                         ┌──────────────────┐
                         │ Final            │
                         │ Classification   │
                         └────────┬─────────┘
                                  ↓
                         ┌──────────────────┐
                         │ Analysis Report  │
                         └──────────────────┘
