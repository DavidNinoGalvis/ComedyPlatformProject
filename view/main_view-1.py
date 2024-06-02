import streamlit as st
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie
from datetime import datetime

# Clase Event para almacenar información de eventos
class Event:
    def __init__(self, name, artist_list, place, date, opening_event_time, direccion, city):
        self.event_name = name
        self.artist = artist_list
        self.event_place = place
        self.event_date = date  
        self.opening_time = opening_event_time
        self.direccion_event = direccion
        self.event_city = city

# Lista global para almacenar eventos
event_list = []

# Función para manejar el inicio de sesión
def login():
    admin_user = "admin"
    admin_password = "admin123"
    account_user = "david"
    account_password = "prueba"
    
    if st.session_state['username'] == admin_user and st.session_state['password'] == admin_password:
        st.session_state['logged_in'] = True
        st.session_state['user_role'] = 'admin'
        st.success("¡Inicio de sesión exitoso como Admin!")
    elif st.session_state['username'] == account_user and st.session_state['password'] == account_password:
        st.session_state['logged_in'] = True
        st.session_state['user_role'] = 'user'
        st.success("¡Inicio de sesión exitoso como Usuario!")
    else:
        st.session_state['logged_in'] = False
        st.error("Usuario o contraseña incorrectos.")

# Interfaz de la página de inicio de sesión
def draw_login_page():
    st.title("Inicio de Sesión")
    with st.form(key="login_form"):
        username = st.text_input("Usuario", key="username_login")
        password = st.text_input("Contraseña", type="password", key="password_login")
        login_button = st.form_submit_button("Iniciar sesión")
        if login_button:
            st.session_state['username'] = username
            st.session_state['password'] = password
            login()

# Función para crear eventos
def create_event_ui():
    with st.form("event_form"):
        name = st.text_input("Nombre del evento")
        artist_list = st.text_input("Lista de artistas (separados por coma)")
        place = st.text_input("Lugar del evento")
        date = st.date_input("Fecha del evento")
        opening_event_time = st.time_input("Hora de apertura")
        direccion = st.text_input("Dirección del evento")
        city = st.text_input("Ciudad del evento")
        submit_button = st.form_submit_button("Crear evento")

        if submit_button:
            artist_list = artist_list.split(",")  # Convertir la cadena de artistas en una lista
            event = Event(name, artist_list, place, date, opening_event_time, direccion, city)
            event_list.append(event)  # Guardar el evento en la lista global
            st.success(f"Evento '{event.event_name}' creado exitosamente!")

# Función para buscar eventos
def search_event_ui():
    st.write("Buscar un evento por nombre:")
    search_name = st.text_input("Nombre del evento a buscar")
    search_button = st.button("Buscar")

    if search_button:
        found_events = [event for event in event_list if search_name.lower() in event.event_name.lower()]
        if found_events:
            st.write(f"Se encontraron {len(found_events)} eventos:")
            for event in found_events:
                st.write(f"Nombre: {event.event_name}, Lugar: {event.event_place}, Fecha: {event.event_date}")
        else:
            st.error("No se encontraron eventos con ese nombre.")

# Función para el saludo condicional según la hora
def saludo_condicional():
    hora_actual = datetime.now().hour
    if hora_actual < 12:
        return "Buenos días: El Show de Gonzorisas"
    elif 12 <= hora_actual < 18:
        return "Buenas tardes: El Show de Gonzorisas"
    else:
        return "Buenas noches: El Show de Gonzorisas"

# Función para la página del administrador
def draw_admin_page():
    if st.session_state['user_role'] == 'admin':
        st.title("Bienvenido, Admin")
        if st.button("Cerrar sesión"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ''
            st.session_state['password'] = ''
            st.session_state['user_role'] = None
        create_event_ui()  # Llamar a la interfaz de creación de eventos
    else:
        st.title("Bienvenido, Usuario")
        st.write("Has iniciado sesión como usuario.")
        if st.button("Cerrar sesión"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ''
            st.session_state['password'] = ''
            st.session_state['user_role'] = None

# Función principal que controla el flujo de la aplicación
def main_admin():
    # Inicializar el estado de la sesión si no existe
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = ''
        st.session_state['password'] = ''
        st.session_state['user_role'] = None
    
    # Control principal de flujo de la página
    if not st.session_state['logged_in']:
        draw_login_page()
    else:
        draw_admin_page()

# Funciones necesarias para utilizar lottie
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def lottieImage():
    lottie_coding = load_lottiefile("static/banner1.json")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )

# Función para la página de inicio
def draw_home_page():
    st.write("Bienvenidos al show de Gonzorisas")
    col1, col2 = st.columns(2)
    with col1:
        lottieImage()
    with col2:
        st.write("""
        ## Bienvenido a mi página
        Aquí puedes encontrar información sobre eventos, subir archivos, gestionar tareas y configurar ajustes.
        """)

# Función para gestionar el contenido de las páginas
def manage_content_page(selected):
    st.title(f"Pagina de {selected}")
    st.info(saludo_condicional())
    if selected == "Inicio":
        draw_home_page()
    elif selected == "Crear Evento":
        create_event_ui()
    elif selected == "Buscar Evento":
        search_event_ui()
    elif selected == "Reportes":
        st.write("Página de Reportes")

# Función principal para manejar las páginas de eventos
def main_event_page():
    selected = option_menu(None, ["Inicio", "Crear Evento", "Buscar Evento", 'Reportes'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal", key="main-menu")
    manage_content_page(selected)

if __name__ == "__main__":
    main_event_page()
