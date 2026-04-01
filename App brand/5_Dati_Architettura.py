import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
import pandas as pd
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

st.title("DATI & ARCHITETTURA")
st.markdown("*Il dato vive nel perimetro licenze del cliente.*")
st.markdown("---")

st.write(
    "Notung non rivende dati grezzi. Consegna software, connettori e segnali derivati. "
    "Il dato vive nel perimetro licenze del cliente — nessun obbligo di redistribuzione. "
    "Modello operativo: BYOD (Bring Your Own Data)."
)

st.markdown("---")
st.subheader("PROVIDER ENTERPRISE")

providers = pd.DataFrame(
    {
        "Provider": [
            "Bloomberg B-PIPE",
            "LSEG / Refinitiv",
            "FactSet",
            "S&P Capital IQ",
            "SIX Financial",
            "Morningstar",
        ],
        "Integrazione": [
            "SDK proprietario (blpapi)",
            "REST API moderna",
            "REST API documentata",
            "REST API (Swagger)",
            "Feed SFTP / API enterprise",
            "REST API",
        ],
        "Complessità": [
            "Alta — richiede IT",
            "Bassa",
            "Bassa–media",
            "Bassa–media",
            "Media",
            "Bassa–media",
        ],
        "Tipico cliente SGR": [
            "SGR gestione attiva, desk trading",
            "SGR mid-size, research-driven",
            "Portfolio management, quant-fondamentale",
            "Credit research, private markets",
            "Complementare, forte su Europa",
            "Più rilevante per fondi",
        ],
    }
)

st.dataframe(providers, use_container_width=True, hide_index=True)

st.info(
    "Bloomberg è un caso a parte — non è una REST API. Richiede terminale fisico attivo, "
    "B-UNIT o Bloomberg Cloud. Coinvolgimento IT obbligatorio dal giorno zero."
)

st.markdown("---")
st.subheader("FONTI OPEN (GESTIBILI DIRETTAMENTE)")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown(
        """
- **ECB Data Portal** — macro EU, overlay macro, regime detection
- **ALFRED (St. Louis Fed)** — macro USA, indicatori economici storici
- **BLS** — labour market USA
"""
    )
with col_b:
    st.markdown(
        """
- **SEC EDGAR** — fondamentali USA, filing
- **OpenFIGI / GLEIF** — security master, entity resolution
"""
    )

st.markdown("---")
st.subheader("STACK AZURE")

col_infra, col_process = st.columns(2)

with col_infra:
    st.markdown("**INFRASTRUTTURA**")
    st.markdown(
        """
- **Azure Function** — motore automatico giornaliero, nessun intervento manuale
- **Blob Storage + Parquet** — archivio immutabile dati raw, garantisce point-in-time per backtest
- **Azure SQL Database** — storico segnali con forward return reale per tracking performance
- **App Service** — dashboard Streamlit/Dash accessibile via browser, sempre aggiornata
- **Key Vault** — credenziali mai nel codice, mai visibili a Notung
"""
    )

with col_process:
    st.markdown("**PROCESSO**")
    st.markdown(
        """
- **GitHub (repo privato per cliente)** — codice sempre versionato e tracciato
- **3 ambienti separati** — locale → staging → produzione. Il codice non va mai direttamente in produzione
- **CI/CD via GitHub** — push su staging aggiorna staging, merge su main aggiorna produzione
- **UAT formale** — il cliente verifica i requisiti concordati in Fase 1, approva via email
- **Gate commerciale** — accettazione scritta → fattura → promozione in produzione
"""
    )

st.markdown("---")
st.subheader("APPROFONDIMENTI")

assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")

dl_col1, dl_col2, dl_col3 = st.columns(3)

with dl_col1:
    fp = os.path.join(assets_dir, "Integrazione Data provider terzi.docx")
    with open(fp, "rb") as f:
        st.download_button(
            label="↓ INTEGRAZIONE DATA PROVIDER",
            data=f,
            file_name="Integrazione Data provider terzi.docx",
            mime="application/octet-stream",
        )

with dl_col2:
    fp = os.path.join(assets_dir, "Ricerca di mercato Data provider SGR e SIM.pdf")
    with open(fp, "rb") as f:
        st.download_button(
            label="↓ RICERCA DATA PROVIDER SGR/SIM",
            data=f,
            file_name="Ricerca di mercato Data provider SGR e SIM.pdf",
            mime="application/octet-stream",
        )

with dl_col3:
    fp = os.path.join(assets_dir, "Notung Guida Tecnica.docx")
    with open(fp, "rb") as f:
        st.download_button(
            label="↓ GUIDA TECNICA",
            data=f,
            file_name="Notung Guida Tecnica.docx",
            mime="application/octet-stream",
        )
