import streamlit as st

# Import pages
from Tabs import home, BT

# Page config
st.set_page_config(
    page_title="BrainScanAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Custom CSS for Premium Look
st.markdown("""
<style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(17, 17, 17, 0.95) !important;
    }

    /* Card/Block Container Styling */
    .block-container {
        padding: 3rem 5rem;
    }

    /* Glassmorphism Metrics */
    [data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 198, 255, 0.4);
    }

    /* Text Colors */
    h1, h2, h3, p, span {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
Tabs = {
    "Home": home,
    "Brain Tumor": BT
}

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(Tabs.keys()))

# Load selected page
Tabs[selection].app()