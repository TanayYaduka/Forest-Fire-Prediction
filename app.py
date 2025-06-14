{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3cb7866-2fbe-47a6-b3ad-8b564599d484",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-14 13:01:23.951 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from tensorflow.keras.models import load_model\n",
    "from PIL import Image, ImageOps\n",
    "\n",
    "# Set up app config\n",
    "st.set_page_config(page_title=\"Fire Detection from Satellite\", layout=\"centered\")\n",
    "\n",
    "st.title(\"Fire Detection from Satellite Images\")\n",
    "st.write(\"Upload a satellite image to detect presence of Fire or Not Fire\")\n",
    "\n",
    "# Load model (cache it)\n",
    "@st.cache_resource\n",
    "def load_fire_model():\n",
    "    model = load_model(\"wildfire_model.h5\")\n",
    "    return model\n",
    "\n",
    "model = load_fire_model()\n",
    "\n",
    "# Class labels (you can update this to match your training config)\n",
    "class_names = [\"No Fire\", \"Fire 🔥\"]\n",
    "\n",
    "# Upload image section\n",
    "uploaded_file = st.file_uploader(\"📷 Upload Satellite Image\", type=[\"jpg\", \"png\", \"jpeg\"])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    image = Image.open(uploaded_file).convert(\"RGB\")\n",
    "    st.image(image, caption=\"Uploaded Image\", use_column_width=True)\n",
    "\n",
    "    # Preprocessing (based on how your model was trained!)\n",
    "    # Replace input shape according to your model\n",
    "    input_shape = (64, 64)  # Change if your model expects something else\n",
    "\n",
    "    # Preprocess image\n",
    "    image_resized = image.resize(input_shape)\n",
    "    img_array = np.array(image_resized) / 255.0\n",
    "    img_array = img_array.reshape(1, *input_shape, 3)  # Add batch dimension\n",
    "\n",
    "    if st.button(\"🧠 Detect Fire\"):\n",
    "        with st.spinner(\"Analyzing image...\"):\n",
    "            prediction = model.predict(img_array)\n",
    "            predicted_class = np.argmax(prediction)\n",
    "            confidence = float(prediction * 100) if predicted_class == 1 else float(1 - prediction) * 100\n",
    "            if confidence < 0.01:\n",
    "                confidence_display = \"< 0.01%\"\n",
    "            else:\n",
    "                confidence_display = f\"{confidence:.2f}%\"\n",
    "                st.info(f\"Confidence: *{confidence_display}*\")\n",
    "\n",
    "\n",
    "            st.subheader(\"Result:\")\n",
    "            st.success(f\"Prediction: *{class_names[predicted_class]}*\")\n",
    "            st.info(f\"Confidence: *{confidence}%*\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89155347-369c-48bd-bcf5-7932acbd366f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
