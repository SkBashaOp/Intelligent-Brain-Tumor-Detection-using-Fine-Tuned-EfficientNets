import streamlit as st
import imagerec
import streamlit.components.v1 as components

def app():

    st.title("🧠 Brain Tumor Predictor")

    st.markdown("### Types of Brain Tumors:")

    st.info("Glioma: Tumor in brain support cells (glial cells).")
    st.warning("Meningioma: Tumor in brain covering membranes.")
    st.error("Pituitary: Tumor in hormone-controlling gland.")

    uploaded_file = st.file_uploader("📤 Upload MRI Image", type=['jpg','png','jpeg'])

    # Sidebar dataset link
    st.sidebar.markdown(
        '<a href="https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: blue; color: white; text-decoration: none; border-radius: 6px;">Dataset</a>',
        unsafe_allow_html=True
    )

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded MRI", use_column_width=True)

    if st.button("🔍 Detect Condition"):

        if uploaded_file is None:
            st.warning("⚠️ Please upload an image first")
            return

        with st.spinner("Analyzing MRI..."):

            # 🔥 REAL MODEL PREDICTION
            y, conf = imagerec.imagerecognise(uploaded_file)

        # Confidence bar
        st.progress(int(conf * 100))
        st.success(f"Confidence: {conf:.2%}")

        # LOW CONFIDENCE CHECK
        if conf < 0.80:
            st.error("❌ Invalid MRI or unclear image. Try a better scan.")
            return

        # RESULT DISPLAY
        if y == "No Tumor":
            components.html("""
                <h1 style='color:green;'>✅ No Tumor Detected</h1>
            """)

        elif y == "Glioma":
            components.html("""
                <h1 style='color:red;'>⚠️ Glioma Detected</h1>
            """)
            st.info("Radiation + chemotherapy may be required.")

        elif y == "Meningioma":
            components.html("""
                <h1 style='color:red;'>⚠️ Meningioma Detected</h1>
            """)
            st.info("Often treatable via surgery and radiation.")

        elif y == "Pituitary":
            components.html("""
                <h1 style='color:red;'>⚠️ Pituitary Tumor Detected</h1>
            """)
            st.info("Hormone therapy or surgery may be needed.")

        # Sidebar confidence
        st.sidebar.warning(f"Model Confidence: {conf:.2%}")