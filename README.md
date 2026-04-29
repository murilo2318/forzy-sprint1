# ⚙️ Forzy Digital Twin — Sprint 1

> **Fundamentos do Ativo e Interface de Cadastro**  
> Disciplina: Front End & Mobile Development — FIAP  
> Framework: Streamlit · Python 3.13

---

## 📋 Sobre o Projeto

O **Forzy Digital Twin** é uma interface web para gestão de motores industriais. Nesta primeira sprint, o objetivo é permitir que operadores cadastrem equipamentos, consultem suas fichas técnicas e visualizem dados brutos dos sensores convertidos em unidades reais (Volts, Ampères, RPM).

---

## 🎯 Requisitos Atendidos

| Requisito | Status |
|-----------|--------|
| Tela inicial com lista de equipamentos | ✅ |
| Módulo de cadastro técnico completo | ✅ |
| Visualização de dados brutos dos sensores | ✅ |
| Arquitetura desacoplada (features/pipelines/providers) | ✅ |
| Sidebar com menu de navegação | ✅ |
| UX com cores semânticas e feedback ao usuário | ✅ |
| Dados de sensores convertidos em unidades reais | ✅ |

---

## 🗂️ Estrutura do Projeto

```
forzy-sprint1/
├── app.py                          # Orquestrador principal
├── requirements.txt                # Dependências
│
├── state/
│   └── session.py                  # Variáveis de sessão (st.session_state)
│
├── ui/
│   └── sidebar.py                  # Menu lateral de navegação
│
├── features/
│   ├── lista/page.py               # Tela 1 — Lista de equipamentos
│   ├── cadastro/page.py            # Tela 2 — Formulário de cadastro técnico
│   └── sensores/page.py            # Tela 3 — Visualização de dados dos sensores
│
├── pipelines/
│   └── equipamento_pipeline.py     # Camada de orquestração (features ↔ providers)
│
└── providers/
    ├── equipamento_provider.py     # Fonte de dados dos equipamentos (in-memory)
    └── sensor_provider.py          # Simulação de leituras dos sensores IoT
```

### Fluxo de Dados

```
app.py → ui/sidebar → features/* → pipelines → providers
```

Essa separação permite evoluir o backend (trocar dados simulados por banco real) sem mexer nas telas, e migrar de framework sem mexer nos dados.

---

## 🖥️ Telas

### 1. Lista de Equipamentos
- Tabela interativa com seleção de linha
- Botões contextuais habilitados apenas com equipamento selecionado
- Navegação para Ficha Técnica ou Sensores

### 2. Cadastro Técnico
- Formulário completo com campos elétricos e mecânicos
- Suporte a modo **novo** e modo **edição**
- Validação de campos obrigatórios com feedback visual
- Cores semânticas: 🟢 Operacional · 🟡 Em Manutenção · ⚫ Desligado

### 3. Dados dos Sensores
- Leitura atual com `st.metric` para 5 grandezas
- Histórico de 24h com gráfico de linha
- Alertas automáticos baseados em limites ISO 10816:
  - Temperatura: ⚠️ > 75°C · 🔴 > 90°C
  - Vibração: ⚠️ > 4.5 mm/s · 🔴 > 7.1 mm/s

---

## ⚙️ Como Rodar

### Pré-requisitos
- Python 3.13
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/murilo2318/forzy-sprint1.git
cd forzy-sprint1

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python3.13 -m streamlit run app.py
```

Acesse em: [http://localhost:8501](http://localhost:8501)

---

## 📦 Dependências

```
streamlit
pandas
numpy
```

---

## 🏭 Equipamentos de Exemplo

O sistema já vem com dois motores pré-cadastrados para demonstração:

| TAG | Modelo | Fabricante | Potência | Status |
|-----|--------|------------|----------|--------|
| MTR-001 | WEG W22 160L | WEG | 25 cv | Operacional |
| MTR-002 | Siemens 1LE1 200L | Siemens | 50 cv | Em Manutenção |

---

## 👨‍💻 Autores

<img width="442" height="133" alt="image" src="https://github.com/user-attachments/assets/195b2e63-93af-48a7-a520-21ff9814d6b3" />

— FIAP · Front End & Mobile Development
