# 🔥 Forest Fire Detection App

A deep learning-based web application for detecting forest fires from satellite images. This project was built using **Jupyter Notebook** for model development and deployed with **Streamlit** for an interactive user interface.

## 📂 Dataset

**Wildfire Prediction Dataset**  
Source: [Kaggle](https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset)

---

## 🛠️ Tools and Technologies

| Tool/Library   | Purpose                                      |
|----------------|----------------------------------------------|
| Python 3.12     | Programming language                         |
| Jupyter Notebook | Model development and testing              |
| TensorFlow (Keras) | Deep learning model training (`.h5` file) |
| Streamlit      | Building and deploying the web interface     |
| NumPy          | Numerical processing                         |
| Pillow (PIL)   | Image loading and preprocessing              |

---

## 🚀 Features

- Upload satellite images (`.jpg`, `.png`, `.jpeg`)
- Predicts whether the image shows **Fire 🔥** or **No Fire**
- Displays prediction result and confidence score
- Responsive and user-friendly Streamlit interface

---

## 📊 App Workflow

1. **Model Loading**  
   Loads the pretrained model `wildfire_model.h5` using TensorFlow.

2. **Image Upload**  
   Users upload a satellite image via the Streamlit UI.

3. **Image Preprocessing**  
   - Converts image to RGB
   - Resizes to `(64x64)` pixels
   - Normalizes pixel values and reshapes for model input

4. **Prediction**  
   - Model outputs prediction for "Fire" or "No Fire"
   - Displays result and confidence level

---

## 🧪 Requirements

Install dependencies using `pip install -r requirements.txt`

```txt
streamlit
tensorflow
pillow
numpy
