import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.title("⚙️ Forzy")
        st.caption("Digital Twin · Motores")
        st.markdown("---")

        if st.button("🏠 Equipamentos", use_container_width=True):
            st.session_state.page = "lista"

        if st.button("➕ Novo Equipamento", use_container_width=True):
            st.session_state.tag_selecionada = None
            st.session_state.modo_cadastro = "novo"
            st.session_state.page = "cadastro"

        st.markdown("---")
        st.caption("Sprint 1 — Fundamentos")