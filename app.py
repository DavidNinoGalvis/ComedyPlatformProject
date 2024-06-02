# Punto de entrada de la aplicación
import streamlit as st

from controllers.gui_controler import GUIController


st.set_page_config(page_title="El Show de Gonzorisas", layout='wide', initial_sidebar_state='collapsed', page_icon="🤣")
if __name__ == "__main__":
    st.markdown("""
    <style>
    .stButton button {
        background-color: #007BFF;
        color: white;
    }
    #navbarSupportedContent ul li a {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    gui = GUIController()
    gui.main()
