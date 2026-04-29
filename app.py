import streamlit as st
from state.session import init_session
from ui.sidebar import render_sidebar
import features.lista.page as lista_page
import features.cadastro.page as cadastro_page
import features.sensores.page as sensores_page

st.set_page_config(
    page_title="Forzy · Digital Twin",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()
render_sidebar()

page = st.session_state.page

if page == "lista":
    lista_page.render()
elif page == "cadastro":
    cadastro_page.render()
elif page == "sensores":
    sensores_page.render()