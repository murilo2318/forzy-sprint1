import streamlit as st


def init_session():
    if "page" not in st.session_state:
        st.session_state.page = "lista"

    if "tag_selecionada" not in st.session_state:
        st.session_state.tag_selecionada = None

    if "modo_cadastro" not in st.session_state:
        st.session_state.modo_cadastro = "novo"