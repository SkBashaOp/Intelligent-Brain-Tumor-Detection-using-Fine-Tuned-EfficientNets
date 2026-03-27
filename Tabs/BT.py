import streamlit as st
import imagerec
import pandas as pd

def app():

    # 🔥 HEADER
    st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🧠 NeuroScanAI</h1>
    <p style='text-align: center; font-size:18px;'>
    AI-powered Brain Tumor Detection using EfficientNetB3
    </p>
    <hr>
    """, unsafe_allow_html=True)

    st.subheader("Types of Brain Tumors")

    st.info("Glioma: Tumor in brain support cells (glial cells).")
    st.warning("Meningioma: Tumor in brain covering membranes.")
    st.error("Pituitary: Tumor in hormone-controlling gland.")

    # 📤 Upload
    uploaded_file = st.file_uploader("📤 Upload MRI Image", type=['jpg','png','jpeg'])

    # Sidebar dataset link
    st.sidebar.markdown(
        '<a href="https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: blue; color: white; text-decoration: none; border-radius: 6px;">Dataset</a>',
        unsafe_allow_html=True
    )

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded MRI", use_column_width=True)

    # 🔍 Prediction Button
    if st.button("🔍 Detect Condition"):

        if uploaded_file is None:
            st.warning("⚠️ Please upload an image first")
            return

        # 🔄 Loading
        with st.spinner("🧠 Analyzing MRI with AI..."):
            y, conf, probs = imagerec.imagerecognise(uploaded_file)

        # 📊 Layout
        col1, col2 = st.columns(2)

        with col1:
            st.image(uploaded_file, caption="MRI Scan", use_column_width=True)

        with col2:
            st.subheader("🧾 Prediction Result")
            st.write(f"**Tumor Type:** {y}")
            st.write(f"**Confidence:** {conf:.2%}")

        # 📈 Confidence
        st.subheader("🔬 Confidence Score")
        st.progress(int(conf * 100))
        st.metric(label="Confidence", value=f"{conf:.2%}")

        # 📊 Probability chart
        df = pd.DataFrame({
            "Tumor Type": ['Glioma','Meningioma','No Tumor','Pituitary'],
            "Probability": probs
        })

        st.subheader("📊 Prediction Breakdown")
        st.bar_chart(df.set_index("Tumor Type"))

        # ⚠️ Low confidence check
        if conf < 0.80:
            st.error("❌ Invalid MRI or unclear image. Try a better scan.")
            return

        # 🎯 Result display
        if y == "No Tumor":
            st.success("✅ No Tumor Detected")
        elif y == "Glioma":
            st.error("⚠️ Glioma Detected")
        elif y == "Meningioma":
            st.warning("⚠️ Meningioma Detected")
        elif y == "Pituitary":
            st.error("⚠️ Pituitary Tumor Detected")

        # 📌 Sidebar confidence
        st.sidebar.warning(f"Model Confidence: {conf:.2%}")

        # 📄 Features section
        st.markdown("""
        ### 🚀 Features
        - EfficientNetB3 Deep Learning Model  
        - ~99% Accuracy (IEEE Published)  
        - Real-time MRI Analysis  
        - Multi-class Tumor Classification  
        """)

        # ⚠️ Disclaimer
        st.markdown("""
        ---
        ⚠️ **Disclaimer**:  
        This AI model is for educational purposes only.  
        Not a substitute for professional medical diagnosis.
        """)