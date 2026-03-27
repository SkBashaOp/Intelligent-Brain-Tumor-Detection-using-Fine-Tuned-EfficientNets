# Intelligent Brain Tumor Detection using Fine-Tuned EfficientNets

## Overview
This project leverages **Deep Learning** to detect and classify brain tumors from MRI scans with high precision. By utilizing a **Fine-Tuned EfficientNetB3** architecture, the model can accurately identify three major types of tumors: **Glioma, Meningioma, and Pituitary tumors**, as well as differentiate them from **Safe (Healthy)** scans.

## Key Features
- **Accurate Classification**: Differentiates between Glioma, Meningioma, Pituitary tumors, and Healthy scans.
- **Robust Validation**: Implements a confidence threshold (95%) to ensure the uploaded image is a valid Brain MRI scan.
- **Medical Insights**: Provides brief medical descriptions and suggested treatment paths for each detection.
- **User-Friendly Interface**: Built with **Streamlit** for seamless interaction and instant results.

## Technology Stack
- **Deep Learning**: TensorFlow/Keras (EfficientNetB3)
- **Web App**: Streamlit
- **Data Processing**: NumPy, OpenCV
- **Visualization**: Matplotlib

## Dataset
The model was trained on the [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset) from Kaggle, encompassing a diverse set of MRI images for various tumor types.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/SkBashaOp/Intelligent-Brain-Tumor-Detection-using-Fine-Tuned-EfficientNets.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Intelligent-Brain-Tumor-Detection-using-Fine-Tuned-EfficientNets
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run main.py
   ```

## Usage
- Open the app in your browser (usually at `http://localhost:8501`).
- Navigate to the **Brain Tumor** page.
- Upload a clear MRI scan in JPG, PNG, or JPEG format.
- Click **Detect Condition** to see the model's prediction and medical insights.

---
*Disclaimer: This tool is intended for educational purposes and research only. It should not be used as a substitute for professional medical diagnosis.*
