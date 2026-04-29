import providers.equipamento_provider as eq_provider
import providers.sensor_provider as sensor_provider

COLUNAS_TABELA = ["TAG", "Modelo", "Fabricante", "Potência (cv)", "Tensão (V)", "Local", "Status"]
COLUNAS_SENSORES = ["Timestamp", "Tensão (V)", "Corrente (A)", "Temp (°C)", "Vibração (mm/s)", "RPM"]


def listar_para_tabela() -> list[list]:
    equipamentos = eq_provider.listar_todos()
    return [
        [
            e["tag"],
            e["modelo"],
            e["fabricante"],
            e["potencia_cv"],
            e["tensao_v"],
            e["local"],
            e["status"],
        ]
        for e in equipamentos
    ]


def salvar_equipamento(*campos) -> str:
    nomes = ["tag", "modelo", "fabricante", "potencia_cv", "tensao_v",
             "corrente_nominal_a", "rotacao_rpm", "fator_potencia",
             "classe_isolamento", "ip", "peso_kg", "local", "status"]
    dados = dict(zip(nomes, campos))
    sucesso, mensagem = eq_provider.salvar(dados)
    return ("✅ " if sucesso else "❌ ") + mensagem


def carregar_equipamento(tag: str) -> dict | None:
    return eq_provider.buscar_por_tag(tag)


def leitura_sensores_para_tabela(tag: str) -> list[list]:
    eq = eq_provider.buscar_por_tag(tag)
    status = eq["status"] if eq else "Operacional"
    historico = sensor_provider.historico_simulado(tag, status)
    return [
        [
            h["timestamp"],
            h["tensao_v"],
            h["corrente_a"],
            h["temp_c"],
            h["vibracao_mms"],
            h["rotacao_rpm"],
        ]
        for h in historico
    ]


def leitura_atual(tag: str) -> dict:
    eq = eq_provider.buscar_por_tag(tag)
    status = eq["status"] if eq else "Operacional"
    return sensor_provider.leitura_atual(tag, status)