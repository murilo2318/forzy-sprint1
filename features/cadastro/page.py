import streamlit as st
import pipelines.equipamento_pipeline as pipeline

FABRICANTES = ["WEG", "Siemens", "ABB", "Nidec", "Outro"]
CLASSES = ["A", "B", "F", "H"]
IPS = ["IP21", "IP44", "IP54", "IP55", "IP65", "IP66"]
TENSOES = [220, 380, 440, 480, 690]
STATUS = ["Operacional", "Em Manutenção", "Desligado"]


def render():
    modo = st.session_state.get("modo_cadastro", "novo")
    tag = st.session_state.get("tag_selecionada")

    st.title("🔧 Cadastro Técnico")

    if st.button("← Voltar para Equipamentos"):
        st.session_state.page = "lista"
        st.rerun()

    st.markdown("---")

    # Carrega dados se for edição
    eq = pipeline.carregar_equipamento(tag) if modo == "edicao" and tag else {}

    # Ficha técnica (somente leitura em modo edição)
    if modo == "edicao" and eq:
        icone = {"Operacional": "🟢", "Em Manutenção": "🟡", "Desligado": "⚫"}.get(eq["status"], "⚪")
        st.subheader(f"{eq['tag']} — {eq['modelo']}")
        st.caption(f"{icone} {eq['status']} · {eq['fabricante']}")
        st.markdown("---")

    # Formulário
    st.subheader("Identificação")
    col1, col2, col3 = st.columns(3)
    with col1:
        f_tag = st.text_input("TAG *", value=eq.get("tag", ""), placeholder="MTR-004")
    with col2:
        f_modelo = st.text_input("Modelo *", value=eq.get("modelo", ""), placeholder="WEG W22 160L")
    with col3:
        fab_idx = FABRICANTES.index(eq["fabricante"]) if eq.get("fabricante") in FABRICANTES else 0
        f_fabricante = st.selectbox("Fabricante *", FABRICANTES, index=fab_idx)

    st.subheader("⚡ Parâmetros Elétricos")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        f_potencia = st.number_input("Potência (cv) *", value=float(eq.get("potencia_cv", 0.0)), min_value=0.0, step=0.5)
    with col2:
        tensao_idx = TENSOES.index(eq["tensao_v"]) if eq.get("tensao_v") in TENSOES else 1
        f_tensao = st.selectbox("Tensão (V) *", TENSOES, index=tensao_idx)
    with col3:
        f_corrente = st.number_input("Corrente Nominal (A) *", value=float(eq.get("corrente_nominal_a", 0.0)), min_value=0.0, step=0.1)
    with col4:
        f_fp = st.slider("Fator de Potência", 0.6, 1.0, float(eq.get("fator_potencia", 0.86)), step=0.01)

    st.subheader("⚙️ Parâmetros Mecânicos")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        f_rotacao = st.number_input("Rotação (RPM) *", value=int(eq.get("rotacao_rpm", 1760)), min_value=0, step=10)
    with col2:
        classe_idx = CLASSES.index(eq["classe_isolamento"]) if eq.get("classe_isolamento") in CLASSES else 2
        f_classe = st.selectbox("Classe de Isolamento", CLASSES, index=classe_idx)
    with col3:
        ip_idx = IPS.index(eq["ip"]) if eq.get("ip") in IPS else 3
        f_ip = st.selectbox("Grau de Proteção (IP)", IPS, index=ip_idx)
    with col4:
        f_peso = st.number_input("Peso (kg)", value=float(eq.get("peso_kg", 0.0)), min_value=0.0, step=1.0)

    st.subheader("📍 Localização e Status")
    col1, col2 = st.columns([3, 1])
    with col1:
        f_local = st.text_input("Localização", value=eq.get("local", ""), placeholder="Planta A — Linha 1")
    with col2:
        status_idx = STATUS.index(eq["status"]) if eq.get("status") in STATUS else 0
        f_status = st.selectbox("Status", STATUS, index=status_idx)

    st.markdown("---")
    col_salvar, col_limpar, _ = st.columns([1, 1, 4])

    with col_salvar:
        if st.button("💾 Salvar", type="primary", use_container_width=True):
            mensagem = pipeline.salvar_equipamento(
                f_tag, f_modelo, f_fabricante, f_potencia, f_tensao,
                f_corrente, f_rotacao, f_fp, f_classe, f_ip, f_peso,
                f_local, f_status
            )
            if mensagem.startswith("✅"):
                st.success(mensagem)
                st.session_state.tag_selecionada = f_tag.strip().upper()
                st.session_state.modo_cadastro = "edicao"
            else:
                st.error(mensagem)

    with col_limpar:
        if st.button("🗑️ Limpar", use_container_width=True):
            st.session_state.modo_cadastro = "novo"
            st.session_state.tag_selecionada = None
            st.r