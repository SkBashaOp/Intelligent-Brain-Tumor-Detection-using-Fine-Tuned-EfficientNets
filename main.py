import streamlit as st

# Import pages
from Tabs import home, BT

# Page config
st.set_page_config(page_title="MRI Brain Tumor Detection", layout="wide")

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