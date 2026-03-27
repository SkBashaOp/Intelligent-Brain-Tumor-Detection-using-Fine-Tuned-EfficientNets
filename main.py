# Importing the necessary Python modules.
import streamlit as st


st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
🧠 NeuroScanAI
</h1>
<p style='text-align: center; font-size:18px;'>
AI-powered Brain Tumor Detection using EfficientNetB3
</p>
<hr>
""", unsafe_allow_html=True)


# Configure the app
st.set_page_config(
    page_title = 'MRI-Data-Analysis',
    page_icon = 'brain',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, BT



# Dictionary for pages
Tabs = {
    "Home": home,
    "Brain Tumor":BT
   
    
}



# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Call the app funciton of selected page to run
Tabs[page].app()
