import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

st.title("VALUE PROPOSITION")
st.markdown("*Decision support quantitativo su misura.*")
st.markdown("---")

st.write(
    "Notung aiuta SGR, SIM e family office a trasformare una domanda di investimento in un segnale "
    "quantitativo proprietario, validato e immediatamente utilizzabile nel processo decisionale. "
    "Non vende una piattaforma standard né un feed chiuso: costruisce con il cliente il modello, "
    "lo implementa in una soluzione stand-alone e lo rilascia come asset proprietario del cliente."
)

st.markdown("---")
st.subheader("OFFERTA COMMERCIALE")

row1_c1, row1_c2 = st.columns(2)
with row1_c1:
    with st.container(border=True):
        st.markdown("**CUSTOM INDICES**")
        st.write("Progettazione e co-creazione di indici proprietari. L'IP resta al cliente.")

with row1_c2:
    with st.container(border=True):
        st.markdown("**CUSTOM RISK MODELS**")
        st.write("Modelli di rischio customizzati su engine/dati del cliente. Anche as-a-service.")

row2_c1, row2_c2 = st.columns(2)
with row2_c1:
    with st.container(border=True):
        st.markdown("**PIATTAFORME ALTERNATIVE DATA**")
        st.write(
            "Analisi di testi, immagini, dati non strutturati integrati nel processo d'investimento."
        )

with row2_c2:
    with st.container(border=True):
        st.markdown("**SIGNAL DISCOVERY**")
        st.write(
            "Ricerca di pattern statisticamente robusti su universo titoli definito dal cliente."
        )

st.markdown("---")
st.subheader("SELLING POINTS")

selling_points = [
    ("→ ASSET PROPRIETARIO", "Codice, logica e documentazione trasferiti in-house. Nessun lock-in."),
    ("→ CO-SVILUPPO", "Il cliente partecipa alla costruzione. Nessuna black-box."),
    ("→ RAPIDITÀ", "Da firma a sistema live: 10–15 settimane."),
    ("→ OUTPUT AZIONABILE", "Segnali presentabili in comitato investimenti con test e documentazione."),
    ("→ INTEGRAZIONE FLESSIBILE", "Fonti open, vendor esistenti del cliente, alternative data."),
]

for label, desc in selling_points:
    c_label, c_desc = st.columns([1, 10])
    with c_label:
        st.markdown(f"**{label}**")
    with c_desc:
        st.write(desc)

st.markdown("---")
st.subheader("ESEMPI DI DELIVERABLE")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("**GESTIONE ATTIVA**")
    st.markdown(
        """
- Dashboard segnali quantitativi aggiornata ogni mattina
- Piattaforma alternative data (testi, transcript, macro)
- Coverage fondamentale automatizzata
- Estrazione insight da documenti (report, filing, MD&A)
- Portfolio commentary assistita
- Screening ibrido fondamentale/quantitativo
"""
    )

with col_right:
    st.markdown("**GESTIONE PASSIVA**")
    st.markdown(
        """
- Tracking error dashboard in tempo reale
- Report composizione indice automatico
- Alert corporate action e rebalancing
"""
    )
