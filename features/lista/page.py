import streamlit as st
import pandas as pd
import pipelines.equipamento_pipeline as pipeline


def render():
    st.title("📋 Equipamentos Cadastrados")

    col1, col2, _ = st.columns([1, 1, 4])
    with col1:
        if st.button("➕ Novo Equipamento", use_container_width=True):
            st.session_state.tag_selecionada = None
            st.session_state.modo_cadastro = "novo"
            st.session_state.page = "cadastro"
    with col2:
        if st.button("🔄 Atualizar", use_container_width=True):
            st.rerun()

    st.markdown("---")

    dados = pipeline.listar_para_tabela()

    if not dados:
        st.info("Nenhum equipamento cadastrado ainda. Clique em **➕ Novo Equipamento** para começar.")
        return

    df = pd.DataFrame(dados, columns=pipeline.COLUNAS_TABELA)

    st.caption("Selecione uma linha e use os botões abaixo para navegar.")
    evento = st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )

    linhas_selecionadas = evento.selection.rows
    tag_selecionada = None

    if linhas_selecionadas:
        idx = linhas_selecionadas[0]
        tag_selecionada = dados[idx][0]
        st.success(f"✅ Equipamento **{tag_selecionada}** selecionado.")

    col_ficha, col_sensor, _ = st.columns([1, 1, 4])

    with col_ficha:
        if st.button("📝 Ver Ficha Técnica", use_container_width=True, disabled=not tag_selecionada):
            st.session_state.tag_selecionada = tag_selecionada
            st.session_state.modo_cadastro = "edicao"
            st.session_state.page = "cadastro"

    with col_sensor:
        if st.button("📡 Ver Sensores", use_container_width=True, disabled=not tag_selecionada):
            st.session_state.tag_selecionada = tag_selecionada
            st.session_state.page = "sensores"