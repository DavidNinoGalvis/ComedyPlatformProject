import streamlit as st
import hydralit_components as hc
from streamlit_calendar import calendar # Biblioteca Necesaria para representar en calendario
from datetime import datetime, timedelta
from controllers.gestion_controler import GestionController
import time
from streamlit_star_rating import st_star_rating

# Clase que almacenara la informacion totales
gestion_controller = GestionController()

gestion_controller.create_event("Evento Bar", "Remate de Fin de año", "Dirección 1", "2024-06-01", "18:00", "Bar X", "Ciudad Y",4 ,"ticket office")
# Ejemplo de evento para la sustentación
test = gestion_controller.create_event("Evento Filantropico", "Ultimatum de Comedia", "Dirección 2", "2024-06-23", "19:00", "Teatro Z", "Ciudad W", 5, "ticket office")
gestion_controller.create_event("Evento Teatro", "Fucks News Noticreo", "Dirección 3", "2024-08-20", "20:00", "Estadio A", "Ciudad B", 2, "ticket office")


calendar_events = [
    {
        "title": "Remate de Fin de Año",
        "start": "2024-06-20T08:30:00",
        "end": "2024-06-21T08:30:00",
        "resourceId": "a",
    },
    {
        "title": "Testeo de Evento",
        "start": "2024-06-29T08:30:00",
        "end": "2024-06-29T08:31:00",
        "resourceId": "a",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]

def add_event_to_calendar_format(event):
    start_datetime = datetime.strptime(f"{event.event_date} {event.opening_time}", "%Y-%m-%d %H:%M")
    
    # Asumiendo una duración de 1 hora para el evento
    end_datetime = start_datetime + timedelta(hours=1)
    
    # Crear el diccionario en el formato requerido
    calendar_event = {
        "title": event.event_name,
        "start": start_datetime.isoformat(),
        "end": end_datetime.isoformat(),
        "resourceId": "a",  # Ajusta esto según sea necesario
    }
    calendar_events.append(calendar_event)

add_event_to_calendar_format(test)

# --------------------------------------------------------------------------------------------------------------------
# Seccion para Comprar un Ticket como usuario
def draw_buy_ticket_page():
    st.title("¡Compra tu boleta para tus shows favoritos!")
    with st.form(key="buy_ticket_form"):
        client_names = st.text_input("Nombres", placeholder="Name")
        client_last_names = st.text_input("Apellidos", placeholder="Last name")
        price_ticket = st.number_input("Precio del Ticket", placeholder="Ticket Price")
        buyer_id = [client_names, client_last_names]
        category = st.text_input("Categoría", placeholder="Category")
        phase = st.text_input("Fase", placeholder="Phase")
        sale_code = st.text_input("Código de Venta", placeholder="Sale Code")
        payment_method = st.text_input("Método de Pago", placeholder="Payment Method")
        refund_method = st.text_input("Método de Reembolso", placeholder="Refund Method")
        #is_active = True  # Asumimos que el ticket está activo por defecto

        buy_ticket_button = st.form_submit_button("Comprar Boleta")
    
    if buy_ticket_button:
        gestion_controller.create_ticket(price_ticket, buyer_id, category, phase, sale_code, payment_method, refund_method)
        st.success("Boleta Comprada")


# --------------------------------------------------------------------------------------------------------------------
# Secion para Crear Eventos

def draw_create_event_page():
    st.title("Sección Para Crear un Evento")

    # Placeholder para manejar la visibilidad de los elementos del formulario y la animación
    form_placeholder = st.empty()
    loader_placeholder = st.empty()
    error_placeholder = st.empty()

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
        rating = st_star_rating(label = "Calidad del Evento", maxValue = 5, defaultValue = 3, key = "rating", dark_theme = True )
        submit_button = st.form_submit_button("Create Event")


    if submit_button:
        # Validaciones de los campos
        #if not name or not option_event or not address or not date or not opening_time or not place_name or not city or capacity <= 0 or ticket_price <= 0:
            #error_placeholder.error("Todos los campos son obligatorios y deben tener valores válidos.")
        #else:
            # Ocultar el formulario y mostrar la animación
            form_placeholder.empty()
            with loader_placeholder.container():
                with hc.HyLoader('Creando Evento', hc.Loaders.standard_loaders, index=[0]):
                    time.sleep(2)
            
            # Crear el evento usando el controlador
            #try:
            event = gestion_controller.create_event(option_event, name, address, date, opening_time, place_name, city, ticket_price, rating)
            #add_event_to_calendar_format(event)
            loader_placeholder.empty()
            form_placeholder.empty()
            with form_placeholder.container():
                st.success("¡El Evento ha sido creado correctamente!")
                st.write(f"Nombre del Evento: {name}")
                st.write(f"Tipo de Evento: {option_event}")
                st.write(f"Dirección: {address}")
                st.write(f"Fecha: {date}")
                st.write(f"Hora de Apertura: {opening_time}")
                st.write(f"Nombre del Establecimiento: {place_name}")
                st.write(f"Ciudad: {city}")
                st.write(f"Capacidad Máxima: {capacity}")
                st.write(f"Precio del Ticket: {ticket_price}")
            #except ValueError as e:
                #error_placeholder.error(str(e))

def draw_modify_event_page():
    st.title("Sección Para Modificar Eventos")
    
    search_option = st.radio("Seleccione una opción de búsqueda:", ("Buscar por nombre", "Seleccionar de una lista"))
    
    if search_option == "Buscar por nombre":
        event_name = st.text_input("Ingrese el nombre del evento para buscar:")
        if st.button("Buscar"):
            event, event_type = gestion_controller.find_event_by_name(event_name)
            if event:
                modify_event_form(event, event_type, event_name)
            else:
                st.error("Evento no encontrado")
    else:
        event_names = gestion_controller.list_events("Bar") + gestion_controller.list_events("Philanthropic") + gestion_controller.list_events("Theater")
        event_name = st.selectbox("Seleccione un evento para modificar:", event_names)
        if event_name:
            event, event_type = gestion_controller.find_event_by_name(event_name)
            if event:
                modify_event_form(event, event_type, event_name)

def modify_event_form(event, event_type, event_name):
    # Verificar y convertir event_date a datetime.date si es necesario
    if isinstance(event.event_date, str):
        event_date = datetime.strptime(event.event_date, "%Y-%m-%d").date()
    elif isinstance(event.event_date, datetime):
        event_date = event.event_date.date()
    else:
        event_date = event.event_date
    
    # Campos de entrada para modificar el evento
    new_name = st.text_input("Nombre:", value=event.event_name)
    new_date = st.date_input("Fecha:", value=event_date)
    new_address = st.text_input("Dirección:", value=event.event_address)
    new_opening_time = st.text_input("Hora de Apertura:", value=event.opening_time)
    new_place_name = st.text_input("Nombre del Lugar:", value=event.place_name)
    new_city = st.text_input("Ciudad:", value=event.event_city)
    new_description = st.text_area("Descripción:", value=event.description if hasattr(event, 'description') else "")
    new_rating = st_star_rating("Ingresa la nueva calidad del evento", maxValue=5, defaultValue=event.rating, key="new_rating")
    
    if st.button("Guardar cambios"):
        gestion_controller.update_event(
            event_type,
            event_name,
            name=new_name,
            date=new_date,
            address=new_address,
            opening_time=new_opening_time,
            place_name=new_place_name,
            city=new_city,
            rating=new_rating,
            description=new_description
        )
        st.success("¡Evento actualizado exitosamente!")
        
        # Mostrar los detalles del evento actualizado
        updated_event = gestion_controller.visualize_event(event_type, new_name)
        st.write("Detalles del evento actualizado:")
        st.write({
            "Nombre": updated_event.event_name,
            "Fecha": updated_event.event_date,
            "Dirección": updated_event.event_address,
            "Hora de Apertura": updated_event.opening_time,
            "Nombre del Lugar": updated_event.place_name,
            "Ciudad": updated_event.event_city,
            "Descripción": updated_event.description if hasattr(updated_event, 'description') else "",
            "Rating del Evento": updated_event.rating
        })

def draw_view_all_events_page():
    st.title("Todos los Eventos")
    
    def display_event(event):
        st.subheader(event.event_name)
        st.write(f"**Tipo de Evento:** {event.__class__.__name__}")
        st.write(f"**Dirección:** {event.event_address}")
        st.write(f"**Fecha:** {event.event_date}")
        st.write(f"**Hora de Apertura:** {event.opening_time}")
        st.write(f"**Nombre del Establecimiento:** {event.place_name}")
        st.write(f"**Ciudad:** {event.event_city}")
        st.write(f"**Rating for Event:** {event.rating}")
        #Users can not change the amout of selected stars
        st_star_rating(label = "Calidad Del Evento", maxValue = 5, defaultValue = event.rating, key = f"rating{event.event_name}", read_only = True )
        #st.write(f"**Capacidad Máxima:** {event.ticket_office.capacity}")
        #st.write(f"**Precio del Ticket:** {event.ticket_office.price:.2f}")
        st.write("---")
    
    def display_ticket(ticket):
        st.subheader(f"Ticket ID: {ticket.buyerID}")
        st.write(f"**Precio:** {ticket.price}")
        st.write(f"**Categoría:** {ticket.category}")
        st.write(f"**Fase:** {ticket.phase}")
        st.write(f"**Código de Venta:** {ticket.saleCode}")
        st.write(f"**Método de Pago:** {ticket.paymentMethod}")
        st.write(f"**Método de Reembolso:** {ticket.refundMethod}")
        #st.write(f"**Activo:** {'Sí' if ticket.isActive else 'No'}")
        st.write("---")
    
    st.header("Eventos")
    all_events = gestion_controller.event_data_base  # Método que asume que retorna todos los eventos
    
    if all_events:
        for event in all_events:
            display_event(event)
    else:
        st.info("No hay eventos disponibles para mostrar.")
    
    st.header("Tickets")
    all_tickets = gestion_controller.tickets  # Asume que tienes una lista de tickets en gestion_controller
    
    if all_tickets:
        for ticket in all_tickets:
            display_ticket(ticket)
    else:
        st.info("No hay tickets disponibles para mostrar.")
# --------------------------------------------------------------------------------------------------------------------------------
# Sección Inicial de la pagina
def draw_home_page():
    st.title("Bienvenidos a Sin Gonzo No hay Comedia")

    # CSS para ajustar el tamaño de la imagen y mejorar el padding de las columnas
    st.markdown(
        """
        <style>
        img {
            border-radius: 35%;  /* Esquinas redondeadas */
            width: 80%;          /* Ajusta este valor según sea necesario para controlar el tamaño de la imagen */
            margin: 10px auto;   /* Centra la imagen y añade un margen alrededor */
        }
        .stButton>button {
            height: 3em;
            width: 100%;
            margin: 2px 0;
        }
        .stLinkButton>button {
            background-color: #E1306C;  /* Color de fondo: Instagram Pink */
            color: white;              /* Color del texto */
            border: none;              /* Sin bordes */
            border-radius: 10px;       /* Bordes redondeados */
            padding: 10px 20px;        /* Padding interno */
            font-size: 16px;           /* Tamaño del texto */
            font-weight: bold;         /* Negrita */
        }
        /* Hover effects */
        .stLinkButton > button:hover {
            background-color: #c72a7c;  /* Un tono más oscuro cuando se pasa el mouse */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("¿Qué es 'Sin Gonzo No hay Comedia'?")
        st.write("""
            'Sin Gonzo No hay Comedia' es una plataforma dedicada a ofrecer eventos de comedia únicos y memorables.
            Aquí podrás comprar boletos, ver información de próximos eventos y mucho más. Únete a nosotros para
            disfrutar de noches llenas de risas y entretenimiento.
        """)
        st.markdown("### Próximos Eventos")
        st.write("Descubre los eventos de comedia que tenemos preparados para ti y asegura tu entrada ahora mismo.")
        if st.button('Ver Eventos'):
            st.write("Aquí podrías redirigir a los usuarios a la página de eventos.")
                
        st.markdown("### ¡Conoce Nuestras Redes Sociales!")
        sub_columns = st.columns(4)
        with sub_columns[0]:
            st.link_button("instagram", "https://www.instagram.com/")
        with sub_columns[1]:
            st.button("Facebook", key="button_facebook")
        with sub_columns[2]:
            st.button("Tik Tok", key="button_tiktok")
        with sub_columns[3]:
            st.button("Youtube", key="button_youtube")
    with col2:
        st.image("docs/logo_main.jpg", caption="Logo de Sin Gonzo No hay Comedia")
        pass
# --------------------------------------------------------------------------------------------------------------------
# Sección para consultar los eventos ya creados

def draw_consult_event_page():
    st.title("Sección para Consultar eventos disponibles")
    cc = st.columns([5,1,8])
    with cc[0]:
        st.subheader("Buscar por Atributos")
        nombre = st.text_input("Nombre del Evento:", placeholder="Event Name")
        search_button = st.button("Buscar", key="searchButton")
        if search_button:
            st.info("test")
    with cc[1]:
        st.markdown("<p>   </p>", unsafe_allow_html=True)
    with cc[2]:
        st.subheader("Calendario de Eventos - Registros")
        calendar_options = {
            "editable": "true",
            "selectable": "true",
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "dayGridDay,dayGridWeek,dayGridMonth",
            },
            "slotMinTime": "06:00:00",
            "slotMaxTime": "18:00:00",
            "initialView": "dayGridMonth",
            "resourceGroupField": "building",
            "resources": [
                {"id": "a", "building": "Building A", "title": "Building A"},
                {"id": "b", "building": "Building A", "title": "Building B"},
                {"id": "c", "building": "Building B", "title": "Building C"},
                {"id": "d", "building": "Building B", "title": "Building D"},
                {"id": "e", "building": "Building C", "title": "Building E"},
                {"id": "f", "building": "Building C", "title": "Building F"},
            ],
        }
        custom_css="""
            .fc-event-past {
                opacity: 0.8;
            }
            .fc-event-time {
                font-style: italic;
            }
            .fc-event-title {
                font-weight: 700;
            }
            .fc-toolbar-title {
                font-size: 2rem;
            }
        """

        calendar1 = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
        st.write(calendar1)

#----------------------------------------------------------------------------------------------------------------------------------------
# Sección para consultar los reportes de ventas
def draw_consult_report_page():
    st.title("Sección Para consultar los reportes de ventas")
    st.header("Prueba de Impresion de eventos")

#----------------------------------------------------------------------------------------------------------------------------------------------
def draw_main_view():
    # Estilos Para todas las paginas como un layout.py
    st.markdown("""
        <style>
        h1 {
            font-family: 'Arial', sans-serif;
            text-align: center;
            font-weight: bold;
            margin-bottom: 50px;
            line-height: 1.5;
            text-shadow: 2px 2px 4px #000000;
            
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown(""""</br>""", unsafe_allow_html=True) # Salto de linea para evitar que se inicie abajo de la navbar fija
    # Definir el menú principal
    menu_data = [
        {'icon': "fa fa-ticket-alt", 'label': "Comprar Boleta"},
        {'icon': "fa fa-calendar-alt", 'label': "Consultar Evento"},
        {'icon': "fa fa-plus-circle", 'label': "Crear Evento"},
        {'icon': "fa fa-edit", 'label': "Modificar Evento"},
        {'icon': "fa fa-chart-line", 'label': "Consultar Reportes"},
        {'icon': "fa fa-chart-line", 'label': "Test - Events"}
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
    # Section Manager - Navigator Bar
    if (menu_id == "Home"):
        draw_home_page()
    elif (menu_id == "Comprar Boleta"):
        draw_buy_ticket_page()
    elif (menu_id == "Consultar Evento"):
        draw_consult_event_page()
    elif (menu_id == "Crear Evento"):
        draw_create_event_page()
    elif (menu_id == "Modificar Evento"):
        draw_modify_event_page()
    elif (menu_id == "Consultar Reportes"):
        pass
    elif (menu_id == "Test - Events"):
        draw_view_all_events_page()