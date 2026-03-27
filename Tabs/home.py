"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Intelligent Brain Tumor Detection using Fine-Tuned EfficientNets")

    # Add image to the home page
    st.image('images/home.png')

    st.markdown('''
    Brain tumors are among the most serious and life-threatening medical conditions. Early and accurate detection is critical for effective treatment and improved patient outcomes.
    
    This application utilizes a **Fine-Tuned EfficientNet** deep learning model, optimized for mobile and web performance via **TensorFlow Lite (TFLite)**. Our system can accurately classify MRI scans into four distinct categories:
    
    1. **Glioma**: Primary brain tumors originating from glial cells.
    2. **Meningioma**: Typically benign tumors arising from the protective membranes.
    3. **Pituitary Tumor**: Abnormal growths in the pituitary gland affecting hormone regulation.
    4. **No Tumor (Safe)**: Healthy brain MRI scans with no detectable abnormalities.

    ### How it Works:
    - **Advanced Image Processing**: Scans are pre-processed and normalized for peak model performance.
    - **Deep Learning Inference**: The EfficientNet architecture analyzes complex spatial patterns in MRI images.
    - **Instant Results**: Provides rapid classification with associated confidence scores to assist in preliminary analysis.
    ''')
    

    
    st.sidebar.markdown(
    f'<a href="https://braintumor.org/support-services/support-groups/brain-tumor-support-conversations/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: blue; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Brain Tumour Health Assistance</a>',
    unsafe_allow_html=True
)
    
    