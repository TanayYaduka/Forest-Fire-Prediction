# 🔥 Forest Fire Detection App

A deep learning-based web application for detecting forest fires from satellite images. This project was developed in **Jupyter Notebook** and deployed using **Streamlit** for a simple and interactive interface.

---

## 📂 Dataset

**Wildfire Prediction Dataset**  
🔗 [Kaggle Link](https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset)

This dataset includes satellite images labeled as either "Fire" or "No Fire" and was used to train a Convolutional Neural Network (CNN) model for binary classification.

---

## 🛠️ Tools and Technologies

| Tool/Library       | Purpose                                      |
|--------------------|----------------------------------------------|
| Python 3.12        | Core programming language                    |
| Jupyter Notebook   | Model development and testing environment    |
| TensorFlow (Keras) | Building and training the CNN model          |
| Streamlit          | Building and deploying the web interface     |
| NumPy              | Numerical operations and image array handling|
| Pillow (PIL)       | Image processing and resizing                |

---

## 🚀 Features

- Upload satellite images in `.jpg`, `.png`, or `.jpeg` formats.
- Predicts presence of **Fire 🔥** or **No Fire** using a trained CNN model.
- Displays prediction result with confidence score.
- Intuitive and responsive web interface built with Streamlit.

---

## 📊 App Workflow

1. **Model Loading**  
   Loads a pre-trained TensorFlow model (`wildfire_model.h5`).

2. **Image Upload**  
   Users upload a satellite image through the Streamlit interface.

3. **Preprocessing**  
   - Converts image to RGB  
   - Resizes to `(64x64)` pixels  
   - Normalizes pixel values  
   - Reshapes image to match model input shape

4. **Prediction**  
   - Predicts the class label (Fire or No Fire)  
   - Displays result with a confidence percentage

---

## 🧪 Requirements

Install all dependencies using the following command:

```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**
```
streamlit
tensorflow
pillow
numpy
```

---

## ▶️ Run the App

To launch the Streamlit app on your local machine, follow these steps:

1. **Clone the repository or download the project files.**
2. Ensure the following files are in the same directory:
   - `app.py`
   - `wildfire_model.h5`
   - `requirements.txt`

3. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the app using Streamlit:**

```bash
streamlit run app.py
```

5. Open the provided local URL in your browser (usually `http://localhost:8501`).

---

## 📸 Example Output

After uploading a satellite image (e.g., a `.jpg` or `.png`), the app displays:

- ✅ **Prediction**: *Fire 🔥* or *No Fire*
- 📊 **Confidence**: e.g., *94.75%*
- 🖼️ The **uploaded image** for visual confirmation

```text
Prediction: Fire 🔥
Confidence: 94.75%
```

The output is shown in a clean, centered layout with proper visual feedback for users.

---

## 📌 Notes

- The uploaded image is resized to **64x64** pixels (or the input shape used during model training).
- The app uses `@st.cache_resource` to optimize model loading and improve performance.
- The TensorFlow model must match the preprocessing steps used in the app (resizing, normalization).

---

## 📬 Contact

For questions, suggestions, or contributions, feel free to open an issue or submit a pull request. Contributions are always welcome!