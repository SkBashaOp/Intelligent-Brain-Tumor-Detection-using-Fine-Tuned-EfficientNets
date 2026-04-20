"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def app():
    """This function creates the upgraded home page"""

    # Hero Section
    st.markdown("""
        <div style="text-align:center; padding: 2rem 0rem;">
            <h1 style="font-size: 3.5rem; background: -webkit-linear-gradient(#00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                BrainScanAI
            </h1>
            <p style="font-size:1.5rem; color: #a0aec0;">
                Next-Generation Brain Tumor Detection powered by Fine-Tuned EfficientNets
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Lottie Animation
    lottie_brain = load_lottie("https://assets2.lottiefiles.com/packages/lf20_2glqweqs.json")
    if lottie_brain:
        st_lottie(lottie_brain, height=300, key="brain_animation")

    st.markdown("---")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("🚀 Our Mission")
        st.write("""
        Early detection of brain tumors can save lives. Our system leverages state-of-the-art 
        deep learning to provide rapid, preliminary MRI analysis, helping clinicians 
        and researchers identify potential abnormalities with surgical precision.
        """)
        st.image('images/home.png', caption="Advanced Neural Processing", use_container_width=True)

    with col2:
        st.subheader("🛠️ Technical Prowess")
        st.markdown('''
        - **EfficientNetB3**: Fine-tuned architecture for high-accuracy medical imaging.
        - **Edge Optimized**: Lightweight TFLite implementation for instant inference.
        - **Multi-Class Detection**: Identifies Gliomas, Meningiomas, and Pituitary tumors.
        - **Robust Validation**: Built-in OOD (Out-of-Distribution) detection for non-MRI images.
        ''')
        
        st.info("💡 **Ready to scan?** Head over to the 'Brain Tumor' tab in the navigation menu.")

    st.sidebar.markdown(
        '<a href="https://braintumor.org/" target="_blank" style="display: block; padding: 12px; background: linear-gradient(90deg, #00c6ff, #0072ff); color: white; text-align: center; text-decoration: none; font-weight: bold; border-radius: 8px;">Support & Resources</a>',
        unsafe_allow_html=True
    )