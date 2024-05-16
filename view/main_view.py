import streamlit as st
#from model import Event
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie

class Event:
    def __init__(self, name, artist_list, place,date,opening_event_time, direccion,city):
        self.event_name = name
        self.artist = artist_list
        self.event_place = place
        self.event_date = date  
        self.opening_time = opening_event_time
        self.direccion_event = direccion
        self.event_city = city

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
    with st.form(key="login_form1"):
        username = st.text_input("Usuario", key="username_login")
        password = st.text_input("Contraseña", type="password", key="password_login")
        login_button = st.form_submit_button("Iniciar sesión")
        if login_button:
            st.session_state['username'] = username
            st.session_state['password'] = password
            login()

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
            st.success(f"Evento '{event.event_name}' creado exitosamente!")

# Interfaz de la página del admin
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


def draw_menu_page(selected):
    st.title(f"Pagina de {selected}")
    st.write(f"Pagina {selected}")
    if selected == "Inicio":
        st.write("Bienvenidos al show de Gonzorisas")
        col1, col2 = st.columns(2)
        with col1:
            lottieImage()
        with col2:
            st.write("""
            ## Bienvenido a mi página
            Aquí puedes encontrar información sobre eventos, subir archivos, gestionar tareas y configurar ajustes.
            """)
    elif selected == "Crear Evento":
        st.write("Complete el siguiente formulario para crear un nuevo evento:")
        
        # Crear un formulario para ingresar los datos del evento
        with st.form("create_event_form"):
            event_name = st.text_input("Nombre del evento")
            artist_list = st.text_input("Artistas (separados por comas)")
            place = st.text_input("Lugar del evento")
            date = st.date_input("Fecha del evento")
            opening_event_time = st.time_input("Hora de apertura del evento")
            direccion = st.text_input("Dirección")
            city = st.text_input("Ciudad")
            
            # Botón para enviar el formulario
            submitted = st.form_submit_button("Crear Evento")
            
            if submitted:
                # Convertir la lista de artistas en una lista de strings
                artist_list = artist_list.split(',')
                # Crear una instancia del evento
                new_event = Event(event_name, artist_list, place, date, opening_event_time, direccion, city)
                st.success(f"Evento '{new_event.event_name}' creado con éxito!")
                st.write(f"Detalles del evento:\nNombre: {new_event.event_name}\nArtistas: {', '.join(new_event.artist)}\nLugar: {new_event.event_place}\nFecha: {new_event.event_date}\nHora de apertura: {new_event.opening_time}\nDirección: {new_event.direccion_event}\nCiudad: {new_event.event_city}")



def main_event_page():
    draw_event_page()

def draw_event_page():
    selected = option_menu(None, ["Inicio", "Crear Evento", "Buscar Evento", 'Reportes'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    selected
    draw_menu_page(selected)


        
