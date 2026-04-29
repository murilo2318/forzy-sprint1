import random
from datetime import datetime, timedelta

_PERFIS: dict[str, dict] = {
    "Operacional": {
        "tensao":   (380, 8),
        "corrente": (40,  3),
        "temp":     (62,  4),
        "vibracao": (2.1, 0.4),
        "rpm":      (1760, 15),
    },
    "Em Manutenção": {
        "tensao":   (0,  0),
        "corrente": (0,  0),
        "temp":     (28, 2),
        "vibracao": (0,  0),
        "rpm":      (0,  0),
    },
    "Desligado": {
        "tensao":   (380, 2),
        "corrente": (0,   0),
        "temp":     (30,  2),
        "vibracao": (0.1, 0.05),
        "rpm":      (0,   0),
    },
}


def _ruido(base: float, sigma: float) -> float:
    return round(max(0.0, base + random.gauss(0, sigma)), 2)


def leitura_atual(tag: str, status: str = "Operacional") -> dict:
    perfil = _PERFIS.get(status, _PERFIS["Operacional"])
    return {
        "tag":          tag,
        "timestamp":    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tensao_v":     _ruido(*perfil["tensao"]),
        "corrente_a":   _ruido(*perfil["corrente"]),
        "temp_c":       _ruido(*perfil["temp"]),
        "vibracao_mms": _ruido(*perfil["vibracao"]),
        "rotacao_rpm":  _ruido(*perfil["rpm"]),
    }


def historico_simulado(tag: str, status: str = "Operacional", n: int = 24) -> list[dict]:
    agora = datetime.now()
    historico = []
    for i in range(n, 0, -1):
        leitura = leitura_atual(tag, status)
        leitura["timestamp"] = (agora - timedelta(hours=i)).strftime("%Y-%m-%d %H:%M")
        historico.append(leitura)
    return historico