import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

st.title("COME SI COSTRUISCE")
st.markdown("*Dalla domanda di investimento al sistema live.*")
st.markdown("---")

# Fase 1
c_num, c_content = st.columns([1, 8])
with c_num:
    st.markdown("## 1")
with c_content:
    st.subheader("DISEGNO DEL PROGETTO")
    st.markdown("*1–2 settimane*")
    st.write(
        "Si trasforma la domanda di investimento in un'ipotesi testabile. "
        "Dataset, metriche di successo e criteri di validazione concordati per iscritto."
    )

st.divider()

# Fase 2
c_num, c_content = st.columns([1, 8])
with c_num:
    st.markdown("## 2")
with c_content:
    st.subheader("RICERCA E PROTOTIPO")
    st.markdown("*3–5 settimane*")
    st.write(
        "Sviluppo del modello in locale. Backtest rigoroso con test statistici, analisi di robustezza. "
        "Il decision memo è il gate: se il segnale non regge, la Fase 3 non parte."
    )
    st.info(
        "Il cliente non paga la Fase 3 se la Fase 2 non porta risultati — "
        "questo va dichiarato esplicitamente nel contratto."
    )

st.divider()

# Fase 3
c_num, c_content = st.columns([1, 8])
with c_num:
    st.markdown("## 3")
with c_content:
    st.subheader("DEPLOYMENT")
    st.markdown("*4–6 settimane*")
    st.write(
        "Il prototipo diventa un sistema live su Azure del cliente. "
        "Motore automatico, magazzino dati, dashboard web. "
        "Il codice è proprietà del cliente dalla prima riga."
    )

st.divider()

# Fase 4
c_num, c_content = st.columns([1, 8])
with c_num:
    st.markdown("## 4")
with c_content:
    st.subheader("INTEGRAZIONE API")
    st.markdown("*1–3 settimane*")
    st.write(
        "Connessione ai vendor dati del cliente (Bloomberg, Refinitiv, FactSet). "
        "Tempi e complessità dipendono dal provider — Bloomberg richiede assessment infrastrutturale separato."
    )

st.divider()

# Fase 5
c_num, c_content = st.columns([1, 8])
with c_num:
    st.markdown("## 5")
with c_content:
    st.subheader("MONITORING & EVOLUTION")
    st.markdown("*Continuativo*")
    st.write(
        "Il segnale viene monitorato nel tempo per drift. "
        "Il sistema viene aggiornato, nuove release gestite con processo formale."
    )

st.markdown("---")
st.subheader("APPROFONDIMENTO")

assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
filepath = os.path.join(assets_dir, "Notung Manuale Operativo.docx")
with open(filepath, "rb") as f:
    st.download_button(
        label="↓ SCARICA MANUALE OPERATIVO",
        data=f,
        file_name="Notung Manuale Operativo.docx",
        mime="application/octet-stream",
    )
