# Punto de entrada de la aplicación
import streamlit as st

from controllers.gui_controler import GUIController

st.set_page_config(page_title="El Show de Gonzorisas",
                   page_icon="🤣")

if __name__ == "__main__":
    gui = GUIController()
    gui.main()
