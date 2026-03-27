"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st


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
