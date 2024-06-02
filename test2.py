import streamlit as st
import hydralit_components as hc
from datetime import datetime
import time

def draw_create_event_page():
    st.title("Sección Para Crear un Evento")

    # Placeholder para manejar la visibilidad de los elementos del formulario y la animación
    form_placeholder = st.empty()
    loader_placeholder = st.empty()

    def show_form():
        with form_placeholder.form(key="event_creation_form"):
            name = st.text_input("Nombre del Evento", placeholder="Enter event name")
            option_data = [
                {'icon': "bi bi-cup-straw", 'label': "Evento Bar"},
                {'icon': "fa fa-theater-masks", 'label': "Evento Teatro"},
                {'icon': "fa fa-hand-holding-heart", 'label': "Evento Filantropico"},
            ]
            st.write("Selecciona el tipo de evento")
            option_event = hc.option_bar(option_definition=option_data, key='PrimaryOption', horizontal_orientation=True)

            address = st.text_input("Dirección Del Evento", placeholder="Enter event address")
            date = st.date_input("Fecha del Evento", value=datetime.today())
            opening_time = st.time_input("Hora de Apertura")
            place_name = st.text_input("Nombre el establecimiento", placeholder="Enter place name")
            city = st.text_input("Ciudad del Evento", placeholder="Enter event city")
            capacity = st.number_input("Capacidad Maxima", min_value=0)
            ticket_price = st.number_input("Precio de Ticket", min_value=0.0, format="%.2f")
            
            num_artists = st.number_input("Number of Artists", min_value=0, step=1)
            artists = []
            for i in range(num_artists):
                artist_name = st.text_input(f"Artist {i+1} Name", placeholder="Enter artist name")
                artist_genre = st.text_input(f"Artist {i+1} Genre", placeholder="Enter artist genre")
                if artist_name and artist_genre:
                    pass
            
            submit_button = st.form_submit_button("Create Event")
            return submit_button, name, option_event, address, date, opening_time, place_name, city, capacity, ticket_price

    submit_button, name, option_event, address, date, opening_time, place_name, city, capacity, ticket_price = show_form()

    if submit_button:
        # Ocultar el formulario y mostrar la animación
        form_placeholder.empty()
        with loader_placeholder.container():
            with hc.HyLoader('Creando Evento', hc.Loaders.standard_loaders, index=[0]):
                time.sleep(2)
        
        # Mostrar el mensaje de éxito y los detalles del evento después de la animación
        form_placeholder.empty()
        with form_placeholder.container():
            st.success("Event Created Successfully!")
            st.write(f"Nombre del Evento: {name}")
            st.write(f"Tipo de Evento: {option_event}")
            st.write(f"Dirección: {address}")
            st.write(f"Fecha: {date}")
            st.write(f"Hora de Apertura: {opening_time}")
            st.write(f"Nombre del Establecimiento: {place_name}")
            st.write(f"Ciudad: {city}")
            st.write(f"Capacidad Máxima: {capacity}")
            st.write(f"Precio del Ticket: {ticket_price}")

# Sección Inicial de la pagina
def draw_home_page():
    st.title("Bienvenidos a Sin Gonzo No hay Comedia")  # Mejorar los Titulos

# Sección para consultar los eventos ya creados
def draw_consult_event_page():
    pass

# Section Manager - Navigator Bar
def draw_main_view():
    st.markdown("</br>", unsafe_allow_html=True)  # Salto de linea para evitar que se inicie abajo de la navbar fija
    # Definir el menú principal
    menu_data = [
        {'icon': "far fa-copy", 'label': "Comprar Boleta"},
        {'icon': "🐙", 'label': "Consultar Evento"},
        {'icon': "far fa-chart-bar", 'label': "Crear Evento"},
        {'icon': "far fa-cart-shopping", 'label': "Modificar Evento"},
        {'icon': "fas fa-tachometer-alt", 'label': "Consultar Reportes"}
    ]

    # Configurar el tema de la barra de navegación
    over_theme = {'txc_inactive': '#FFFFFF'}

    # Crear la barra de navegación
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        login_name='Logout',
        hide_streamlit_markers=True,
        sticky_nav=True,
        sticky_mode='sticky',
    )
    
    if menu_id == "Home":
        draw_home_page()
    elif menu_id == "Comprar Boleta":
        #draw_buy_ticket_page()
        pass
    elif menu_id == "Consultar Evento":
        draw_consult_event_page()
    elif menu_id == "Crear Evento":
        draw_create_event_page()
    elif menu_id == "Consultar Reportes":
        pass
    elif menu_id == "Crear Eventos1":
        pass

if __name__ == "__main__":
    draw_main_view()
