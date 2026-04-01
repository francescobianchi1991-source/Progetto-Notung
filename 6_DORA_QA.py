import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import streamlit as st
from utils import inject_css, sidebar_brand

inject_css()
sidebar_brand()

st.title("DORA & COMPLIANCE")
st.markdown("*Le domande che ogni compliance officer fa.*")
st.markdown("---")

with st.expander("Siete una piccola realtà senza certificazioni. Come vi inseriamo nel registro fornitori ICT?"):
    st.write(
        "Non siamo un fornitore ICT nel senso che DORA intende. Non ospitiamo i vostri dati, "
        "non gestiamo infrastrutture critiche, non eroghiamo un servizio continuativo in cloud. "
        "Il sistema gira nel vostro Azure, con le vostre credenziali, sotto il vostro controllo. "
        "Il nostro ruolo è paragonabile a quello di un consulente che vi ha scritto del codice — "
        "non a quello di un SaaS da cui dipendete operativamente."
    )

with st.expander("E se Notung chiudesse domani?"):
    st.write(
        "È esattamente il punto su cui siamo strutturalmente più forti di qualsiasi alternativa SaaS. "
        "Se chiudessimo domani: il sistema continua a girare nel vostro Azure, il codice è vostro, "
        "la documentazione è vostra, i dati sono nel vostro storage. "
        "Non dipendete da noi per nessuna funzione operativa quotidiana."
    )

with st.expander("Non avete ISO 27001 né SOC 2. Come gestiamo la due diligence?"):
    st.write(
        "Abbiamo qualcosa di meglio di una certificazione: un'architettura che riduce il perimetro di rischio. "
        "I vostri dati non ci passano mai — restano nel vostro Azure. "
        "Le credenziali le caricate voi nel Key Vault — noi non le vediamo mai in chiaro. "
        "Il nostro accesso è limitato, tracciato tramite Azure AD e revocabile in qualsiasi momento."
    )

with st.expander("Come gestiamo i diritti di audit previsti da DORA?"):
    st.write(
        "Il codice è vostro — potete auditarlo quando volete. "
        "Il sistema gira nel vostro Azure — il vostro IT ha accesso completo a log, dati, infrastruttura. "
        "L'audit right DORA serve per ispezionare quello che il fornitore fa con i vostri dati nel suo ambiente. "
        "Nel nostro modello quell'ambiente è il vostro."
    )

with st.expander("Avete un piano BCP?"):
    st.write(
        "Il BCP per un sistema Notung coincide con il fatto che il sistema non dipende da Notung per girare. "
        "Non c'è un servizio Notung da mantenere attivo — c'è il vostro Azure, "
        "con i propri SLA garantiti da Microsoft (99.9%+ per App Service e Azure Function)."
    )

with st.expander("DORA richiede SLA contrattuali. Cosa garantite?"):
    st.write(
        "SLA di supporto coerenti con le vostre esigenze di processo. "
        "Exit policy formale con consegna di codice, documentazione e dati entro 30 giorni."
    )

with st.expander("Usate librerie open source. Come gestiamo il rischio vulnerabilità?"):
    st.write(
        "Le librerie usate (pandas, numpy, plotly, azure-sdk) sono standard industriali usati da milioni "
        "di applicazioni enterprise, incluse banche e asset manager. "
        "Il codice è nel vostro GitHub — il vostro IT può eseguire vulnerability scan quando vuole. "
        "Aggiornamenti delle dipendenze gestiti ad ogni release e documentati nel CHANGELOG."
    )

st.markdown("---")
st.subheader("DOMANDE COMMERCIALI FREQUENTI")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**COMMERCIALE**")
    with st.expander("Non capisco cosa stai vendendo."):
        st.write(
            "Sono un capability builder. Costruisco un modello quantitativo validato, "
            "lo deplojo nel vostro Azure e ve lo consegno come asset proprietario con codice, "
            "documentazione e monitoring. Il deliverable non è un report — "
            "è un sistema che gira ogni mattina e che resta vostro."
        )
    with st.expander("Il mercato ha già Axyon, MDOTM, Exabel."):
        st.write(
            "Quei vendor vendono output confezionati su universi predefiniti con motori che non controllate. "
            "Io costruisco il segnale con voi, su vostro universo, e ve lo consegno con tutto: "
            "codice, test statistici, documentazione. "
            "Quando il comitato chiede 'come funziona?', avete una risposta."
        )

with col2:
    st.markdown("**BUDGET & ROI**")
    with st.expander("Non ho budget per 'ricerca del segnale'."):
        st.write(
            "Non la mettete a budget come ricerca — la mettete come acquisto di una capability analitica interna. "
            "Il benchmark sono i custom indices: stesso modello — "
            "comprate un asset governato, non un abbonamento a un servizio esterno."
        )
    with st.expander("Come dimostri che il segnale genera valore reale?"):
        st.write(
            "Con numeri e processo: forward return 2.6% vs baseline 0.8%, win rate 63.4%, "
            "parametri scelti prima di guardare i risultati, separazione in-sample/out-of-sample, t-test. "
            "È quello che portate in comitato investimenti — non una promessa, una metodologia difendibile."
        )

with col3:
    st.markdown("**RISCHIO EXECUTION**")
    with st.expander("Progetti bespoke hanno cicli lunghi e outcome incerti."):
        st.write(
            "Gate espliciti: Fase 1 (1–2 settimane) definisce l'ipotesi, "
            "Fase 2 (3–5 settimane) produce un decision memo con verdetto chiaro. "
            "Se il segnale non regge, ci fermiamo — non pagate la Fase 3."
        )
    with st.expander("Il backtest funziona, ma poi live no. Chi si prende la responsabilità?"):
        st.write(
            "Il backtest è una prova statistica, non una garanzia — e questo sta nel contratto. "
            "Garantiamo rigore metodologico e monitoring continuativo per rilevare drift. "
            "Stessa logica dei risk model provider: Axioma non garantisce alpha, "
            "garantisce un modello governato e mantenuto."
        )
