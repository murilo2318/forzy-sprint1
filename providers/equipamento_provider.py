from datetime import datetime
from typing import Optional

_DB: dict[str, dict] = {
    "MTR-001": {
        "tag":                "MTR-001",
        "modelo":             "WEG W22 160L",
        "fabricante":         "WEG",
        "potencia_cv":        25.0,
        "tensao_v":           380,
        "corrente_nominal_a": 42.5,
        "rotacao_rpm":        1760,
        "fator_potencia":     0.86,
        "classe_isolamento":  "F",
        "ip":                 "IP55",
        "peso_kg":            145.0,
        "local":              "Planta A — Linha 1",
        "status":             "Operacional",
        "cadastrado_em":      "2024-11-10",
    },
    "MTR-002": {
        "tag":                "MTR-002",
        "modelo":             "Siemens 1LE1 200L",
        "fabricante":         "Siemens",
        "potencia_cv":        50.0,
        "tensao_v":           440,
        "corrente_nominal_a": 80.0,
        "rotacao_rpm":        1775,
        "fator_potencia":     0.88,
        "classe_isolamento":  "F",
        "ip":                 "IP55",
        "peso_kg":            280.0,
        "local":              "Planta A — Linha 2",
        "status":             "Em Manutenção",
        "cadastrado_em":      "2024-12-01",
    },
}


def listar_todos() -> list[dict]:
    return [dict(eq) for eq in _DB.values()]


def buscar_por_tag(tag: str) -> Optional[dict]:
    entry = _DB.get(tag.strip().upper())
    return dict(entry) if entry else None


def salvar(dados: dict) -> tuple[bool, str]:
    tag = dados.get("tag", "").strip().upper()
    if not tag:
        return False, "TAG de identificação é obrigatória."
    if not dados.get("modelo", "").strip():
        return False, "Modelo do equipamento é obrigatório."
    if not dados.get("fabricante", "").strip():
        return False, "Fabricante é obrigatório."

    eh_novo = tag not in _DB
    data_cadastro = (
        _DB[tag]["cadastrado_em"] if not eh_novo
        else datetime.now().strftime("%Y-%m-%d")
    )

    _DB[tag] = {
        **dados,
        "tag":           tag,
        "cadastrado_em": data_cadastro,
        "status":        dados.get("status", "Operacional"),
    }

    acao = "cadastrado" if eh_novo else "atualizado"
    return True, f"Equipamento {tag} {acao} com sucesso."


def tags_disponiveis() -> list[str]:
    return sorted(_DB.keys())