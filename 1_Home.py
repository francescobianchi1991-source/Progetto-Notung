import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

col_left, col_right = st.columns(2)

with col_left:
    st.title("NOTUNG")
    st.markdown("*Signal over noise.*")
    st.markdown("---")
    st.write(
        "Notung è una boutique specialistica che aiuta SGR, SIM e family office a trasformare "
        "problemi di investimento in insight, segnali quantitativi e strumenti analitici proprietari, "
        "costruiti su misura."
    )
    st.markdown("---")
    st.metric(label="Target", value="SGR · SIM · Family Office")
    st.metric(label="Breakeven", value="2 clienti")
    st.metric(label="Time to live", value="10–15 settimane")

with col_right:
    with st.container(border=True):
        st.subheader("LA PROPOSTA IN SINTESI")
        st.markdown(
            """
- **Asset proprietario** — codice e logica rilasciati in-house, nessun lock-in
- **Co-sviluppo** — il cliente partecipa alla costruzione, nessuna black-box
- **Rapidità** — da firma a sistema live in 10–15 settimane
- **Output azionabili** — segnali presentabili in comitato investimenti
- **Compliance DORA** — architettura client-hosted, nessun ICT provider critico
"""
        )
        st.markdown("---")
        st.subheader("OFFERTA")
        st.markdown(
            "Custom Indices · Custom Risk Models · Alternative Data Platforms · Signal Discovery"
        )
