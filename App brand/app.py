# -*- coding: utf-8 -*-
import streamlit as st
import os

st.set_page_config(page_title="NOTUNG — Signal over noise.", layout="wide", initial_sidebar_state="collapsed")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap');

/* RESET STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp > header {display: none;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stSidebar"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
.stApp {background: #F7F6F3;}

/* FONT GLOBALS */
* {box-sizing: border-box; margin: 0; padding: 0;}
body, .stApp {font-family: 'EB Garamond', Georgia, serif; color: #1C1C1E;}

h1, h2, h3, h4, .coolvetica {
  font-family: 'Barlow Condensed', 'Helvetica Neue', sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* NAV STICKY */
.notung-nav {
  position: sticky;
  top: 0;
  z-index: 999;
  background: #FFFFFF;
  border-bottom: 1px solid #E8E4DC;
  padding: 0 48px;
  display: flex;
  align-items: center;
  gap: 32px;
  height: 52px;
  overflow-x: auto;
  white-space: nowrap;
}
.notung-nav a {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #4A4A52;
  text-decoration: none;
  padding-bottom: 2px;
  transition: color 150ms, border-bottom 150ms;
}
.notung-nav a:hover {
  color: #1B2A4A;
  border-bottom: 2px solid #1B2A4A;
}

/* SECTIONS */
.section {
  padding: 96px 10%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.section-dark {
  background: #1B2A4A;
  color: #FFFFFF;
}
.section-ivory {background: #F7F6F3;}
.section-white {background: #FFFFFF;}

/* SECTION HEADERS */
.section-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 40px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #1C1C1E;
  margin-bottom: 8px;
}
.section-title-dark {color: #FFFFFF;}
.section-subtitle {
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 22px;
  color: #4A4A52;
  margin-bottom: 56px;
  line-height: 1.4;
}
.section-subtitle-dark {color: #B0BDD4;}

/* HERO */
.hero-wrap {
  background: #1B2A4A;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.hero-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 96px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #FFFFFF;
  line-height: 1;
}
.hero-payoff {
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 24px;
  color: #B0BDD4;
  margin-top: 20px;
}

/* POC CARDS */
.poc-card {
  border: 1px solid #1B2A4A;
  padding: 24px;
  background: #FFFFFF;
  cursor: pointer;
  transition: background 200ms, color 200ms;
  margin-bottom: 16px;
  text-decoration: none;
  display: block;
}
.poc-card:hover {background: #1B2A4A;}
.poc-card:hover .poc-title, .poc-card:hover .poc-desc, .poc-card:hover .poc-link {color: #FFFFFF !important;}
.poc-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #1C1C1E;
  margin-bottom: 8px;
}
.poc-desc {
  font-family: 'EB Garamond', serif;
  font-size: 15px;
  color: #4A4A52;
  line-height: 1.5;
  margin-bottom: 12px;
}
.poc-link {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: #1B2A4A;
  text-transform: uppercase;
}

/* MARKET BLOCKS */
.market-block {padding: 0 0 40px 0;}
.col-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #1B2A4A;
  border-bottom: 2px solid #1B2A4A;
  padding-bottom: 8px;
  margin-bottom: 20px;
}
.body-text {
  font-family: 'EB Garamond', serif;
  font-size: 16px;
  line-height: 1.65;
  color: #1C1C1E;
}
.body-text li {margin-bottom: 10px; margin-left: 18px;}

/* DOWNLOAD BLOCK */
.download-section-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #4A4A52;
  margin-bottom: 16px;
  margin-top: 48px;
}

/* OFFER CARDS (2x2) */
.offer-card {
  border-left: 3px solid #1B2A4A;
  padding: 20px 24px;
  background: #FFFFFF;
  margin-bottom: 16px;
}
.offer-card-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #1B2A4A;
  margin-bottom: 8px;
}
.offer-card-body {
  font-family: 'EB Garamond', serif;
  font-size: 15px;
  color: #4A4A52;
  line-height: 1.55;
}

/* STRENGTH BLOCKS */
.strength-block {
  padding: 24px 0;
  border-top: 1px solid #E8E4DC;
}
.strength-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #1B2A4A;
  margin-bottom: 8px;
}

/* TIMELINE */
.timeline-phase {
  position: relative;
  padding: 32px 0 32px 80px;
  border-left: 1px solid #E8E4DC;
  margin-left: 32px;
}
.phase-number {
  position: absolute;
  left: -52px;
  top: 24px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 64px;
  font-weight: 700;
  color: #E8E4DC;
  line-height: 1;
}
.phase-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 16px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #1C1C1E;
}
.phase-duration {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #1B2A4A;
  margin-bottom: 10px;
}
.phase-note {
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 14px;
  color: #4A4A52;
  margin-top: 6px;
}

/* PROVIDER TABLE */
.provider-table {width: 100%; border-collapse: collapse; margin-top: 16px;}
.provider-table th {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #4A4A52;
  border-bottom: 1px solid #E8E4DC;
  padding: 8px 12px;
  text-align: left;
}
.provider-table td {
  font-family: 'EB Garamond', serif;
  font-size: 14px;
  color: #1C1C1E;
  border-bottom: 1px solid #E8E4DC;
  padding: 10px 12px;
  line-height: 1.4;
}
.provider-table tr:last-child td {border-bottom: none;}

/* STACK LIST */
.stack-item {
  display: flex;
  gap: 16px;
  padding: 14px 0;
  border-bottom: 1px solid #E8E4DC;
  align-items: flex-start;
}
.stack-item:last-child {border-bottom: none;}
.stack-label {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #1B2A4A;
  min-width: 180px;
}
.stack-desc {
  font-family: 'EB Garamond', serif;
  font-size: 15px;
  color: #4A4A52;
  line-height: 1.5;
}

/* ACCORDION (DORA / QA) */
.accordion-item {border-bottom: 1px solid #E8E4DC;}
.accordion-q {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #1C1C1E;
  padding: 16px 0;
  cursor: pointer;
}
.accordion-a {
  font-family: 'EB Garamond', serif;
  font-size: 16px;
  color: #1C1C1E;
  background: #FFFFFF;
  padding: 16px 24px;
  border-left: 2px solid #1B2A4A;
  line-height: 1.6;
  margin-bottom: 8px;
}

/* QA COLUMNS */
.qa-col-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #1B2A4A;
  border-bottom: 2px solid #1B2A4A;
  padding-bottom: 8px;
  margin-bottom: 20px;
}
.qa-q {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #1C1C1E;
  margin-top: 20px;
  margin-bottom: 6px;
}
.qa-a {
  font-family: 'EB Garamond', serif;
  font-size: 15px;
  color: #4A4A52;
  line-height: 1.6;
  border-left: 2px solid #E8E4DC;
  padding-left: 14px;
}

/* FOOTER */
.footer-wrap {
  background: #1B2A4A;
  padding: 96px 10%;
  text-align: center;
  min-height: 40vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
}
.footer-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 48px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #FFFFFF;
}
.footer-payoff {
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 18px;
  color: #B0BDD4;
}
.footer-contact {
  font-family: 'EB Garamond', serif;
  font-size: 15px;
  color: #B0BDD4;
  margin-top: 32px;
  line-height: 1.8;
}
.footer-copy {
  font-family: 'EB Garamond', serif;
  font-size: 13px;
  color: #5A6F8A;
  margin-top: 16px;
}

/* SELLING POINTS */
.selling-wrap {display: flex; gap: 0; margin-top: 48px; border-top: 1px solid #E8E4DC;}
.selling-item {
  flex: 1;
  padding: 24px 20px;
  border-right: 1px solid #E8E4DC;
}
.selling-item:last-child {border-right: none;}
.selling-icon {font-size: 20px; margin-bottom: 8px;}
.selling-label {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #1B2A4A;
  margin-bottom: 6px;
}
.selling-desc {
  font-family: 'EB Garamond', serif;
  font-size: 14px;
  color: #4A4A52;
  line-height: 1.5;
}

/* DOWNLOAD BUTTON OVERRIDES */
.stDownloadButton > button {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.1em !important;
  background: #FFFFFF !important;
  color: #1C1C1E !important;
  border: 1px solid #1B2A4A !important;
  border-radius: 0 !important;
  padding: 16px 24px !important;
  width: 100% !important;
  text-align: left !important;
  transition: background 200ms, color 200ms !important;
}
.stDownloadButton > button:hover {
  background: #1B2A4A !important;
  color: #FFFFFF !important;
}

/* EXPANDER STYLE */
[data-testid="stExpander"] {
  border: none !important;
  border-bottom: 1px solid #E8E4DC !important;
  border-radius: 0 !important;
}
[data-testid="stExpander"] summary {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  color: #1C1C1E !important;
  padding: 14px 0 !important;
}
[data-testid="stExpanderDetails"] {
  background: #FFFFFF;
  border-left: 2px solid #1B2A4A;
  padding: 16px 24px;
  font-family: 'EB Garamond', serif;
  font-size: 16px;
  line-height: 1.6;
  color: #1C1C1E;
}
</style>
""", unsafe_allow_html=True)


# ── HELPER: load asset ────────────────────────────────────────────────────────
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

def load_asset(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return None

def download_card(label, filename, mime, doc_type="Documento"):
    data = load_asset(filename)
    if data:
        st.download_button(
            label=f"↓  {label}",
            data=data,
            file_name=filename,
            mime=mime,
            use_container_width=True,
        )
    else:
        st.markdown(f"""
        <div style="border:1px solid #E8E4DC; padding:16px 24px; color:#4A4A52;
                    font-family:'EB Garamond',serif; font-size:14px; font-style:italic;">
          ↓ {label} <span style="font-size:11px;">(file non ancora caricato)</span>
        </div>""", unsafe_allow_html=True)


# ── NAV ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="notung-nav">
  <a href="#genesi">Genesi</a>
  <a href="#mercato">Mercato</a>
  <a href="#value-proposition">Value Proposition</a>
  <a href="#punti-di-forza">Punti di Forza</a>
  <a href="#come-si-costruisce">Come Funziona</a>
  <a href="#dati-architettura">Dati &amp; Architettura</a>
  <a href="#dora">DORA</a>
  <a href="#qa">Q&amp;A</a>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 0 — HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
  <div class="hero-title">NOTUNG</div>
  <div class="hero-payoff">Signal over noise.</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 1 — GENESI
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="genesi"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-ivory">
  <div class="section-title">Da dove nasce l'idea</div>
  <div class="section-subtitle">"Ho compresso mesi di lavoro in settimane."</div>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    st.markdown("""
    <div style="background:#F7F6F3; padding: 0 0 48px 0;">
    <p class="body-text" style="margin-bottom:20px;">
      Ho costruito da solo un framework quantitativo completo: universo dati, feature engineering,
      ricerca di pattern, backtest, validazione statistica. Un team tradizionale ci mette 3–6 mesi.
      Con Claude: una settimana.
    </p>
    <p class="body-text" style="margin-bottom:20px;">
      Robustezza statistica: separazione in-sample/out-of-sample, anti-overfitting, test statistici,
      registry strutturato, survivorship bias esplicitato. Il risultato è qualcosa che un gestore
      può portare in comitato investimenti.
    </p>
    <p class="body-text">
      Claude non è il prodotto. È il moltiplicatore. Io definisco il problema finanziario,
      la struttura metodologica, i criteri di validazione. Claude accelera l'implementazione.
      Il valore intellettuale è mio — difendibile, spiegabile, non replicabile da chiunque
      apra un account.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div style="background:#F7F6F3; padding: 0 0 48px 0;">
    <a href="https://abpqdjywy3gjcfatnwwfyp.streamlit.app/" target="_blank" class="poc-card" style="text-decoration:none;">
      <div class="poc-title">Framework Quantitativo</div>
      <div class="poc-desc">Pattern discovery completo su equity. Backtest, validazione statistica, registry strutturato.</div>
      <div class="poc-link">→ Apri demo</div>
    </a>
    <a href="https://hormuz-monitor-phccjg3pmb3s6mma64qfpv.streamlit.app/" target="_blank" class="poc-card" style="text-decoration:none;">
      <div class="poc-title">Hormuz Monitor</div>
      <div class="poc-desc">Monitoraggio traffico navale nello Stretto di Hormuz come segnale geopolitico.</div>
      <div class="poc-link">→ Apri demo</div>
    </a>
    <a href="https://weather-energy-signal-tvtglnbgvruhsvebmle3rw.streamlit.app/" target="_blank" class="poc-card" style="text-decoration:none;">
      <div class="poc-title">Weather &amp; Energy</div>
      <div class="poc-desc">Dati meteo incrociati con prezzi delle commodity per generazione di segnali.</div>
      <div class="poc-link">→ Apri demo</div>
    </a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 2 — MERCATO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="mercato"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-white">
  <div class="section-title">Il Mercato</div>
  <div class="section-subtitle">"Bisogni reali, soluzioni parziali."</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div style="background:#FFFFFF; padding:0 0 40px 0;">
    <div class="col-title">Cosa manca</div>
    <ul class="body-text" style="list-style:none; padding:0;">
      <li style="margin-bottom:14px;"><strong>Insight dispersi</strong> — Fonti, note, transcript,
      watchlist vivono in flussi separati. Convergere in un output decisionale chiaro è difficile.</li>
      <li style="margin-bottom:14px;"><strong>Workflow lenti</strong> — Parte rilevante del lavoro
      di ricerca resta manuale, poco standardizzata.</li>
      <li><strong>Competenze quant inaccessibili</strong> — I team small/mid non hanno scala
      per costruire internamente.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:#FFFFFF; padding:0 0 40px 0;">
    <div class="col-title">L'offerta esistente</div>
    <ul class="body-text" style="list-style:none; padding:0;">
      <li style="margin-bottom:12px;">Bloomberg / Refinitiv / FactSet — dati standard, costo elevato
      (~$24k/anno), personalizzazione limitata</li>
      <li style="margin-bottom:12px;">Axyon, MDOTM, RavenPack — segnali pronti, black-box,
      non customizzabili</li>
      <li style="margin-bottom:12px;">Exabel, Boosted.ai — workbench quant, richiedono team
      interno strutturato e budget significativi</li>
      <li>Custom indices — accessibili solo a realtà con masse rilevanti</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="background:#FFFFFF; padding:0 0 40px 0;">
    <div class="col-title">I freni all'adozione</div>
    <ul class="body-text" style="list-style:none; padding:0;">
      <li style="margin-bottom:12px;"><strong>Black-box</strong> — Il 65% (survey Assogestioni 2025)
      cita la spiegabilità come ostacolo n.1</li>
      <li style="margin-bottom:12px;"><strong>Customizzazione</strong> — Richiede costi elevati
      e competenze interne</li>
      <li style="margin-bottom:12px;"><strong>Lock-in</strong> — Timore di dipendere da un vendor
      per una fase critica del processo</li>
      <li><strong>Co-sviluppo assente</strong> — Il mercato vende output, non costruisce
      insieme al cliente</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="download-section-title" style="background:#FFFFFF; padding: 0 0 8px 0;">Approfondimenti di mercato</p>', unsafe_allow_html=True)
dl1, dl2 = st.columns(2, gap="medium")
with dl1:
    download_card(
        "Ricerca — insight e segnali quantitativi (Italia)",
        "Ricerca di mercato sul mercato italiano di insight e segnali quantitativi.pdf",
        "application/pdf"
    )
with dl2:
    download_card(
        "Ricerca — provider dati USA ed Europa",
        "Ricerca di mercato sui provider dati per USA ed Europa.pdf",
        "application/pdf"
    )
st.markdown("<div style='height:64px; background:#FFFFFF'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 3 — VALUE PROPOSITION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="value-proposition"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-ivory">
  <div class="section-title">Value Proposition</div>
  <div class="section-subtitle">"Decision support quantitativo su misura."</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#F7F6F3; padding: 0 10% 40px 10%;">
<p class="body-text">
  Notung aiuta SGR, SIM e family office a trasformare una domanda di investimento in un segnale
  quantitativo proprietario, validato e immediatamente utilizzabile nel processo decisionale.
  Non vende una piattaforma standard né un feed chiuso: costruisce con il cliente il modello,
  lo implementa in una soluzione stand-alone e lo rilascia come asset proprietario del cliente.
</p>
</div>
""", unsafe_allow_html=True)

vc1, vc2 = st.columns(2, gap="medium")
with vc1:
    st.markdown("""
    <div style="background:#F7F6F3; padding: 0 0 0 10%;">
    <div class="offer-card">
      <div class="offer-card-title">Custom Indices</div>
      <div class="offer-card-body">Progettazione e co-creazione di indici proprietari. L'IP resta al cliente.</div>
    </div>
    <div class="offer-card">
      <div class="offer-card-title">Custom Risk Models</div>
      <div class="offer-card-body">Modelli di rischio customizzati su engine/dati del cliente. Anche as-a-service.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

with vc2:
    st.markdown("""
    <div style="background:#F7F6F3; padding: 0 10% 0 0;">
    <div class="offer-card">
      <div class="offer-card-title">Piattaforme Alternative Data</div>
      <div class="offer-card-body">Analisi di testi, immagini, dati non strutturati integrati nel processo d'investimento.</div>
    </div>
    <div class="offer-card">
      <div class="offer-card-title">Signal Discovery</div>
      <div class="offer-card-body">Ricerca di pattern statisticamente robusti su universo titoli definito dal cliente.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="background:#F7F6F3; padding: 0 10% 80px 10%;">
<div class="selling-wrap">
  <div class="selling-item">
    <div class="selling-icon">🔒</div>
    <div class="selling-label">Asset Proprietario</div>
    <div class="selling-desc">Codice, logica e documentazione trasferiti in-house. Nessun lock-in.</div>
  </div>
  <div class="selling-item">
    <div class="selling-icon">👁</div>
    <div class="selling-label">Co-sviluppo</div>
    <div class="selling-desc">Il cliente partecipa alla costruzione. Nessuna black-box.</div>
  </div>
  <div class="selling-item">
    <div class="selling-icon">⚡</div>
    <div class="selling-label">Rapidità</div>
    <div class="selling-desc">Da firma a sistema live: 10–15 settimane.</div>
  </div>
  <div class="selling-item">
    <div class="selling-icon">📊</div>
    <div class="selling-label">Output Azionabile</div>
    <div class="selling-desc">Segnali presentabili in comitato investimenti con test e documentazione.</div>
  </div>
  <div class="selling-item">
    <div class="selling-icon">🔗</div>
    <div class="selling-label">Integrazione Dati</div>
    <div class="selling-desc">Fonti open, vendor esistenti del cliente, alternative data.</div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 4 — PUNTI DI FORZA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="punti-di-forza"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-white">
  <div class="section-title">Punti di Forza</div>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3, gap="large")
strengths_left = [
    ("Rapidità", "Soluzione browser-based, stand-alone. Nessuna integrazione con sistemi proprietari richiesta. Operativa in settimane."),
    ("Trasparenza", "Output leggibili, documentabili, difendibili in comitato. Il cliente capisce cosa compra perché ha partecipato a costruirlo."),
]
strengths_mid = [
    ("Sicurezza Statistica", "Modelli progettati con disciplina: separazione in-sample/out-of-sample, test statistici, anti-overfitting, registry tracciabile."),
    ("Personalizzazione", "Ogni progetto nasce da una domanda specifica del cliente. Nessun prodotto uguale per tutti. Integrazione con dati custom del personale."),
]
strengths_right = [
    ("No Lock-In", "Il sistema gira nel vostro Azure. Il codice è vostro dalla prima riga. Se Notung chiudesse domani, il sistema continua a girare."),
    ("Compliance DORA", "Il modello client-hosted riduce sostanzialmente il profilo di rischio DORA. La soluzione viene trasferita in-house: nessun ICT third-party provider critico da registrare."),
]

def render_strengths(col, items):
    with col:
        for title, body in items:
            st.markdown(f"""
            <div class="strength-block" style="background:#FFFFFF;">
              <div class="strength-title">{title}</div>
              <p class="body-text">{body}</p>
            </div>
            """, unsafe_allow_html=True)

render_strengths(s1, strengths_left)
render_strengths(s2, strengths_mid)
render_strengths(s3, strengths_right)

st.markdown('<p class="download-section-title" style="background:#FFFFFF; padding: 32px 0 8px 0;">Approfondimento</p>', unsafe_allow_html=True)
dl_pf, _ = st.columns([1, 1], gap="medium")
with dl_pf:
    download_card(
        "Ricerca — acquistabilità boutique decision support quant",
        "Ricerca di mercato sull'acquistabilità di una boutique di decision support quant.pdf",
        "application/pdf"
    )
st.markdown("<div style='height:64px; background:#FFFFFF'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 5 — COME SI COSTRUISCE
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="come-si-costruisce"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-ivory">
  <div class="section-title">Come si costruisce</div>
  <div class="section-subtitle">"Dalla domanda di investimento al sistema live."</div>
</div>
""", unsafe_allow_html=True)

phases = [
    ("1", "Disegno del Progetto", "1–2 settimane",
     "Si trasforma la domanda di investimento in un'ipotesi testabile. Dataset, metriche di successo e criteri di validazione concordati per iscritto.",
     None),
    ("2", "Ricerca e Prototipo", "3–5 settimane",
     "Sviluppo del modello in locale. Backtest rigoroso con test statistici. Il decision memo è il gate: se il segnale non regge, la Fase 3 non parte.",
     "Il cliente non paga la Fase 3 se la Fase 2 non porta risultati."),
    ("3", "Deployment", "4–6 settimane",
     "Il prototipo diventa un sistema live su Azure del cliente. Motore automatico, magazzino dati, dashboard web. Il codice è proprietà del cliente dalla prima riga.",
     None),
    ("4", "Integrazione API", "1–3 settimane",
     "Connessione ai vendor dati del cliente (Bloomberg, Refinitiv, FactSet). Tempi dipendono dal provider — Bloomberg richiede assessment separato.",
     None),
    ("5", "Monitoring & Evolution", "Continuativo",
     "Il segnale viene monitorato per drift. Nuove release gestite con processo formale.",
     None),
]

timeline_html = '<div style="background:#F7F6F3; padding: 0 10% 40px 10%;">'
for num, title, duration, desc, note in phases:
    note_html = f'<div class="phase-note">⚠ {note}</div>' if note else ""
    timeline_html += f"""
    <div class="timeline-phase">
      <div class="phase-number">{num}</div>
      <div class="phase-title">{title}</div>
      <div class="phase-duration">{duration}</div>
      <p class="body-text">{desc}</p>
      {note_html}
    </div>
    """
timeline_html += "</div>"
st.markdown(timeline_html, unsafe_allow_html=True)

st.markdown('<p class="download-section-title" style="background:#F7F6F3; padding: 16px 10% 8px 10%;">Documentazione</p>', unsafe_allow_html=True)
dl_man, _ = st.columns([1, 1], gap="medium")
with dl_man:
    download_card(
        "Notung Manuale Operativo",
        "Notung Manuale Operativo.docx",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
st.markdown("<div style='height:64px; background:#F7F6F3'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 6 — DATI & ARCHITETTURA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="dati-architettura"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-white">
  <div class="section-title">Dati &amp; Architettura</div>
  <div class="section-subtitle">"Il dato vive nel perimetro licenze del cliente."</div>
</div>
""", unsafe_allow_html=True)

da1, da2 = st.columns(2, gap="large")

with da1:
    st.markdown("""
    <div style="background:#FFFFFF; padding: 0 0 40px 0;">
    <div class="col-title">Modello BYOD</div>
    <p class="body-text" style="margin-bottom:24px;">
      Notung non rivende dati grezzi. Consegna software, connettori e segnali derivati.
      Il dato vive nel perimetro licenze del cliente — nessun obbligo di redistribuzione.
    </p>
    <table class="provider-table">
      <tr>
        <th>Provider</th><th>Integrazione</th><th>Complessità</th>
      </tr>
      <tr><td>Bloomberg B-PIPE</td><td>SDK proprietario (blpapi)</td><td>Alta — richiede IT</td></tr>
      <tr><td>LSEG / Refinitiv</td><td>REST API moderna</td><td>Bassa</td></tr>
      <tr><td>FactSet</td><td>REST API documentata</td><td>Bassa–media</td></tr>
      <tr><td>S&amp;P Capital IQ</td><td>REST API (Swagger)</td><td>Bassa–media</td></tr>
      <tr><td>SIX Financial</td><td>Feed SFTP / API enterprise</td><td>Media</td></tr>
    </table>
    <p class="body-text" style="margin-top:16px; font-style:italic; font-size:14px; color:#4A4A52;">
      Bloomberg è un caso a parte — non è una REST API. Richiede terminale fisico attivo.
      Coinvolgimento IT obbligatorio dal giorno zero.
    </p>
    </div>
    """, unsafe_allow_html=True)

with da2:
    st.markdown("""
    <div style="background:#FFFFFF; padding: 0 0 40px 0;">
    <div class="col-title">Stack Azure</div>
    <div class="stack-item">
      <div class="stack-label">Azure Function</div>
      <div class="stack-desc">Motore automatico giornaliero</div>
    </div>
    <div class="stack-item">
      <div class="stack-label">Blob Storage + Parquet</div>
      <div class="stack-desc">Archivio immutabile dati raw, point-in-time</div>
    </div>
    <div class="stack-item">
      <div class="stack-label">Azure SQL Database</div>
      <div class="stack-desc">Storico segnali con forward return reale</div>
    </div>
    <div class="stack-item">
      <div class="stack-label">App Service</div>
      <div class="stack-desc">Dashboard Streamlit/Dash via browser</div>
    </div>
    <div class="stack-item">
      <div class="stack-label">Key Vault</div>
      <div class="stack-desc">Credenziali mai nel codice, mai visibili a Notung</div>
    </div>
    <div class="stack-item">
      <div class="stack-label">GitHub CI/CD</div>
      <div class="stack-desc">Tre ambienti: locale → staging → produzione</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="download-section-title" style="background:#FFFFFF; padding: 16px 0 8px 0;">Documentazione tecnica</p>', unsafe_allow_html=True)
da_dl1, da_dl2 = st.columns(2, gap="medium")
with da_dl1:
    download_card(
        "Integrazione Data provider terzi",
        "Integrazione Data provider terzi.docx",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
with da_dl2:
    download_card(
        "Ricerca — Data provider SGR e SIM",
        "Ricerca di mercato Data provider SGR e SIM.pdf",
        "application/pdf"
    )
st.markdown("<div style='height:64px; background:#FFFFFF'></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 7 — DORA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="dora"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-ivory">
  <div class="section-title">DORA</div>
  <div class="section-subtitle">"Le domande che ogni compliance officer fa."</div>
</div>
""", unsafe_allow_html=True)

dora_qa = [
    (
        "Siete una piccola realtà senza certificazioni. Come vi inseriamo nel registro fornitori ICT?",
        "Non siamo un fornitore ICT nel senso che DORA intende. Non ospitiamo i vostri dati, non gestiamo infrastrutture critiche, non eroghiamo un servizio continuativo in cloud. Il sistema gira nel vostro Azure, con le vostre credenziali, sotto il vostro controllo. Il nostro ruolo è paragonabile a quello di un consulente che vi ha scritto del codice — non a quello di un SaaS da cui dipendete operativamente."
    ),
    (
        "E se Notung chiudesse domani?",
        "È esattamente il punto su cui siamo strutturalmente più forti di qualsiasi alternativa SaaS. Se chiudessimo domani: il sistema continua a girare nel vostro Azure, il codice è vostro, la documentazione è vostra, i dati sono nel vostro storage. Non dipendete da noi per nessuna funzione operativa quotidiana."
    ),
    (
        "Non avete ISO 27001 né SOC 2. Come gestiamo la due diligence?",
        "Abbiamo qualcosa di meglio di una certificazione: un'architettura che riduce il perimetro di rischio. I vostri dati non ci passano mai — restano nel vostro Azure. Le credenziali le caricate voi nel Key Vault — noi non le vediamo mai in chiaro. Il nostro accesso è limitato, tracciato tramite Azure AD e revocabile in qualsiasi momento."
    ),
    (
        "Come gestiamo i diritti di audit previsti da DORA?",
        "Il codice è vostro — potete auditarlo quando volete. Il sistema gira nel vostro Azure — il vostro IT ha accesso completo a log, dati, infrastruttura. L'audit right DORA serve per ispezionare quello che il fornitore fa con i vostri dati nel suo ambiente. Nel nostro modello quell'ambiente è il vostro."
    ),
    (
        "Avete un piano BCP?",
        "Il BCP per un sistema Notung coincide con il fatto che il sistema non dipende da Notung per girare. Non c'è un servizio Notung da mantenere attivo — c'è il vostro Azure, con i propri SLA garantiti da Microsoft (99.9%+ per App Service e Azure Function)."
    ),
    (
        "DORA richiede SLA contrattuali. Cosa garantite?",
        "SLA di supporto coerenti con le vostre esigenze di processo. Exit policy formale con consegna di codice, documentazione e dati entro 30 giorni."
    ),
    (
        "Usate librerie open source. Come gestiamo il rischio vulnerabilità?",
        "Le librerie usate (pandas, numpy, plotly, azure-sdk) sono standard industriali usati da milioni di applicazioni enterprise, incluse banche e asset manager. Il codice è nel vostro GitHub — il vostro IT può eseguire vulnerability scan quando vuole. Aggiornamenti delle dipendenze gestiti ad ogni release e documentati nel CHANGELOG."
    ),
]

st.markdown('<div style="background:#F7F6F3; padding: 0 10% 80px 10%;">', unsafe_allow_html=True)
for q, a in dora_qa:
    with st.expander(q):
        st.markdown(a)
st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEZIONE 8 — Q&A GENERALI
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div id="qa"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-white">
  <div class="section-title">Domande Frequenti</div>
</div>
""", unsafe_allow_html=True)

qa1, qa2, qa3 = st.columns(3, gap="large")

with qa1:
    st.markdown("""
    <div style="background:#FFFFFF; padding: 0 0 60px 0;">
    <div class="qa-col-title">Commerciale</div>
    <div class="qa-q">Non capisco cosa stai vendendo. Sei un consulente o un software vendor?</div>
    <div class="qa-a">Sono un capability builder. Costruisco un modello quantitativo validato,
    lo deplojo nel vostro Azure e ve lo consegno come asset proprietario con codice, documentazione
    e monitoring. Il deliverable non è un report — è un sistema che gira ogni mattina e che resta vostro.</div>
    <div class="qa-q" style="margin-top:28px;">Il mercato ha già Axyon, MDOTM, Exabel. Perché venire da te?</div>
    <div class="qa-a">Quei vendor vendono output confezionati su universi predefiniti con motori che
    non controllate. Io costruisco il segnale con voi, su vostro universo, e ve lo consegno con tutto:
    codice, test statistici, documentazione. Quando il comitato chiede "come funziona?", avete una risposta.</div>
    </div>
    """, unsafe_allow_html=True)

with qa2:
    st.markdown("""
    <div style="background:#FFFFFF; padding: 0 0 60px 0;">
    <div class="qa-col-title">Budget &amp; ROI</div>
    <div class="qa-q">Non ho budget per "ricerca del segnale".</div>
    <div class="qa-a">Non la mettete a budget come ricerca — la mettete come acquisto di una capability
    analitica interna. Il benchmark sono i custom indices: stesso modello — comprate un asset governato,
    non un abbonamento a un servizio esterno.</div>
    <div class="qa-q" style="margin-top:28px;">Come dimostri che il segnale genera valore reale?</div>
    <div class="qa-a">Con numeri e processo: forward return 2.6% vs baseline 0.8%, win rate 63.4%,
    parametri scelti prima di guardare i risultati, separazione in-sample/out-of-sample, t-test.
    È quello che portate in comitato investimenti — non una promessa, una metodologia difendibile.</div>
    </div>
    """, unsafe_allow_html=True)

with qa3:
    st.markdown("""
    <div style="background:#FFFFFF; padding: 0 0 60px 0;">
    <div class="qa-col-title">Rischio Execution</div>
    <div class="qa-q">Progetti bespoke hanno cicli lunghi e outcome incerti.</div>
    <div class="qa-a">Gate espliciti: Fase 1 (1–2 settimane) definisce l'ipotesi,
    Fase 2 (3–5 settimane) produce un decision memo con verdetto chiaro.
    Se il segnale non regge, ci fermiamo — non pagate la Fase 3.</div>
    <div class="qa-q" style="margin-top:28px;">Il backtest funziona, ma poi live no. Chi si prende la responsabilità?</div>
    <div class="qa-a">Il backtest è una prova statistica, non una garanzia — e questo sta nel contratto.
    Garantiamo rigore metodologico e monitoring continuativo per rilevare drift.
    Stessa logica dei risk model provider: Axioma non garantisce alpha, garantisce un modello governato e mantenuto.</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer-wrap">
  <div class="footer-title">NOTUNG</div>
  <div class="footer-payoff">Signal over noise.</div>
  <div class="footer-contact">
    Per informazioni e proposte di collaborazione scrivere a:<br>
    <a href="mailto:" style="color:#B0BDD4; text-decoration:none;">[inserire indirizzo email]</a>
  </div>
  <div class="footer-copy">© 2025 Notung. Tutti i diritti riservati.</div>
</div>
""", unsafe_allow_html=True)
