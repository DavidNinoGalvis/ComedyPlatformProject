import streamlit as st
import hydralit_components as hc
import datetime
import time

# Configurar la página de Streamlit
st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
st.markdown(""""</br>""", unsafe_allow_html=True) # Salto de linea para evitar que se inicie abajo de la navbar fija
# Definir el menú principal
menu_data = [
    {'icon': "far fa-copy", 'label': "Test 1"},
    {'id': 'Copy', 'icon': "🐙", 'label': "Copy"},
    {'icon': "fa-solid fa-radar", 'label': "Dropdown1", 'submenu': [{'id': 'subid11', 'icon': "fa fa-paperclip", 'label': "Sub-item 1"}, {'id': 'subid12', 'icon': "💀", 'label': "Sub-item 2"}, {'id': 'subid13', 'icon': "fa fa-database", 'label': "Sub-item 3"}]},
    {'icon': "far fa-chart-bar", 'label': "Chart"},
    {'id': 'Crazy return value 💀', 'icon': "💀", 'label': "Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label': "Dashboard", 'ttip': "I'm the Dashboard tooltip!"},
    {'icon': "far fa-copy", 'label': "Right End"},
    {'icon': "fa-solid fa-radar", 'label': "Dropdown2", 'submenu': [{'label': "Sub-item 1", 'icon': "fa fa-meh"}, {'label': "Sub-item 2"}, {'icon': '🙉', 'label': "Sub-item 3"}]},
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

# Agregar un botón para demostrar funcionalidad
if st.button('click me'):
    st.info('You clicked at: {}'.format(datetime.datetime.now()))
    with hc.HyLoader('Creando Evento',hc.Loaders.standard_loaders,index=[0]):
      time.sleep(1)

if st.sidebar.button('click me too'):
    st.info('You clicked at: {}'.format(datetime.datetime.now()))
    with hc.HyLoader('Creando Evento',hc.Loaders.standard_loaders,index=[0]):
      time.sleep(1)

# Contenido de la página
st.info(f"{menu_id}")


for i in range(20):
    st.write(f"{menu_id} para {i}")
