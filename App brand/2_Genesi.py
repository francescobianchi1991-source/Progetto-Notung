import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

st.title("DA DOVE NASCE L'IDEA")
st.markdown("*Ho compresso mesi di lavoro in settimane.*")
st.markdown("---")

col_left, col_right = st.columns([3, 2])

with col_left:
    st.write(
        "Ho costruito da solo un framework quantitativo completo: universo dati, feature engineering, "
        "ricerca di pattern, backtest, validazione statistica. Un team tradizionale ci mette 3–6 mesi. "
        "Con Claude: una settimana."
    )
    st.write(
        "Robustezza statistica: separazione in-sample/out-of-sample, anti-overfitting, test statistici, "
        "registry strutturato, survivorship bias esplicitato. Il risultato è qualcosa che un gestore "
        "può portare in comitato investimenti."
    )
    st.write(
        "Claude non è il prodotto. È il moltiplicatore. Io definisco il problema finanziario, "
        "la struttura metodologica, i criteri di validazione. Claude accelera l'implementazione. "
        "Il valore intellettuale è mio — difendibile, spiegabile, non replicabile da chiunque apra un account."
    )
    st.write(
        "«One-man-band» costituisce un vantaggio: per il cliente small/mid, un team grande significa "
        "costi fissi, riunioni. Io sono direttamente la persona che ha costruito il modello."
    )

with col_right:
    st.subheader("I POC COSTRUITI")

    with st.container(border=True):
        st.markdown("**FRAMEWORK QUANTITATIVO**")
        st.write(
            "Pattern discovery completo su equity. Backtest, validazione statistica, registry strutturato."
        )
        st.link_button("→ APRI DEMO", url="https://abpqdjywy3gjcfatnwwfyp.streamlit.app/")

    with st.container(border=True):
        st.markdown("**HORMUZ MONITOR**")
        st.write(
            "Monitoraggio traffico navale nello Stretto di Hormuz come segnale geopolitico."
        )
        st.link_button("→ APRI DEMO", url="https://hormuz-monitor-phccjg3pmb3s6mma64qfpv.streamlit.app/")

    with st.container(border=True):
        st.markdown("**WEATHER & ENERGY**")
        st.write(
            "Dati meteo incrociati con prezzi delle commodity per generazione di segnali."
        )
        st.link_button("→ APRI DEMO", url="https://weather-energy-signal-tvtglnbgvruhsvebmle3rw.streamlit.app/")
