# NOTUNG — Brief per Claude Code
## App Streamlit: sito di presentazione del progetto

---

## OBIETTIVO

Costruire una single-page app Streamlit che presenti il progetto Notung a potenziali clienti (SGR, SIM, family office). L'app è navigabile come un sito con sezioni scorrevoli, navigazione sticky in cima, e download di documenti allegati. Nessun login, accesso libero.

---

## STRUTTURA FILE PROGETTO

```
notung_app/
├── app.py                  ← file principale Streamlit
├── assets/                 ← documenti scaricabili
│   ├── Notung Manuale Operativo.docx
│   ├── Notung Guida Tecnica.docx
│   ├── Integrazione Data provider terzi.docx
│   ├── Ricerca di mercato Data provider SGR e SIM.pdf
│   ├── Ricerca di mercato sui provider dati per USA ed Europa.pdf
│   ├── Ricerca di mercato sul mercato italiano di insight e segnali quantitativi.pdf
│   └── Ricerca di mercato sull'acquistabilità di una boutique di decision support quant.pdf
└── BRIEF_CLAUDE_CODE.md    ← questo file
```

---

## ISPIRAZIONE VISIVA

Riferimento: https://www.uspsdelivers.com/2020-2021-generational-research-report/

**Cosa prendere:** struttura a sezioni full-viewport con scroll, navigazione sticky, titoli grandi che dominano la sezione, pochissimo testo per sezione, molto respiro. Versione molto più light/semplice, senza animazioni elaborate.

**NON copiare:** animazioni pesanti, sfondi fotografici, stile colorato americano.

---

## BRAND IDENTITY — REGOLE ASSOLUTE

### Palette colori
```
Sfondo primario:      #F7F6F3  (Avorio freddo)
Sfondo alternativo:   #FFFFFF  (Bianco puro)
Sfondo card/sezione:  #E8E4DC  (Tortora)
Testo principale:     #1C1C1E  (Antracite profondo)
Testo secondario:     #4A4A52  (Grafite)
Accento primario:     #1B2A4A  (Blu notte) — usato solo per CTA, border, highlight
Accento secondario:   #2C4A52  (Petrolio) — grafici, varianti
```
Proporzioni: 80% avorio/bianco · 15% antracite/grafite · 5% blu notte.
MAI altri colori. MAI gradienti. MAI colori saturi.

### Tipografia
Usare Google Fonts tramite CSS injection in Streamlit:
- **CoolVetica** → titoli principali, MAIUSCOLO, letter-spacing largo (+0.08em)
- **EB Garamond** → corpo testo, sottotitoli, quote. Regular 1.6 line-height. Corsivo per payoff/citazioni.
- Fallback: Georgia per serif, Helvetica Neue per sans

Gerarchia:
- Display/Hero: CoolVetica, 64-80px, maiuscolo, antracite
- Titolo sezione: CoolVetica, 36-44px, maiuscolo
- Sottotitolo: EB Garamond corsivo, 20-24px
- Corpo: EB Garamond regular, 16-18px, line-height 1.6
- Label/caption: CoolVetica, 11-12px, maiuscolo, letter-spacing +0.12em

### Tono visivo
- "Clinica svizzera d'eccellenza" — precisione, ordine, competenza silenziosa
- "Hotel di lusso minimalista" — calma, qualità percepibile senza ostentazione
- MAI aspetto fintech colorato, MAI stile startup, MAI icone tondeggianti colorate
- Icone: stile lineare sottile (Lucide o Phosphor), solo dove servono per navigazione/struttura

### Payoff
`Signal over noise.` — appare sempre in EB Garamond corsivo

---

## STRUTTURA DELL'APP — SEZIONI

L'app è una pagina unica con navigazione orizzontale sticky in cima.
Ogni sezione occupa almeno una viewport height (min-height: 100vh), sfondo alternato.

### Nav sticky
Voci: `GENESI · MERCATO · VALUE PROPOSITION · PUNTI DI FORZA · COME FUNZIONA · DATI & ARCHITETTURA · DORA · Q&A`
Font: CoolVetica, 11px, maiuscolo, letter-spacing largo
Sfondo nav: #FFFFFF con border-bottom 1px solid #E8E4DC
Voce attiva: border-bottom 2px solid #1B2A4A

---

### SEZIONE 0 — HERO

**Sfondo:** #1B2A4A (Blu notte) — UNICA sezione scura
**Contenuto centrato verticalmente:**

```
NOTUNG
Signal over noise.
```

- `NOTUNG` → CoolVetica, 96px, bianco #FFFFFF, maiuscolo, letter-spacing +0.1em
- `Signal over noise.` → EB Garamond corsivo, 24px, colore #B0BDD4 (bianco attenuato)
- Nessun altro elemento. Puro respiro.

---

### SEZIONE 1 — DA DOVE NASCE L'IDEA

**Sfondo:** #F7F6F3

**Titolo:** `DA DOVE NASCE L'IDEA`
**Sottotitolo EB Garamond corsivo:** *"Ho compresso mesi di lavoro in settimane."*

**Contenuto in 2 colonne:**

Colonna sinistra (testo):
- Paragrafo: Ho costruito da solo un framework quantitativo completo: universo dati, feature engineering, ricerca di pattern, backtest, validazione statistica. Un team tradizionale ci mette 3-6 mesi. Con Claude: una settimana.
- Paragrafo: Robustezza statistica: separazione in-sample/out-of-sample, anti-overfitting, test statistici, registry strutturato, survivorship bias esplicitato. Il risultato è qualcosa che un gestore può portare in comitato investimenti.
- Paragrafo: Claude non è il prodotto. È il moltiplicatore. Io definisco il problema finanziario, la struttura metodologica, i criteri di validazione. Claude accelera l'implementazione. Il valore intellettuale è mio — difendibile, spiegabile, non replicabile da chiunque apra un account.

Colonna destra — **3 card POC cliccabili** (link esterno, apre nuova tab):

**Card 1:**
- Titolo: FRAMEWORK QUANTITATIVO
- Descrizione: Pattern discovery completo su equity. Backtest, validazione statistica, registry strutturato.
- Link: https://abpqdjywy3gjcfatnwwfyp.streamlit.app/
- Etichetta: → Apri demo

**Card 2:**
- Titolo: HORMUZ MONITOR
- Descrizione: Monitoraggio traffico navale nello Stretto di Hormuz come segnale geopolitico.
- Link: https://hormuz-monitor-phccjg3pmb3s6mma64qfpv.streamlit.app/
- Etichetta: → Apri demo

**Card 3:**
- Titolo: WEATHER & ENERGY
- Descrizione: Dati meteo incrociati con prezzi delle commodity per generazione di segnali.
- Link: https://weather-energy-signal-tvtglnbgvruhsvebmle3rw.streamlit.app/
- Etichetta: → Apri demo

**Stile card POC:**
- Bordo 1px solid #1B2A4A
- Padding 24px
- Sfondo #FFFFFF
- Hover: sfondo #1B2A4A, testo bianco (transizione 200ms)
- Titolo: CoolVetica 13px maiuscolo
- Descrizione: EB Garamond 15px
- Link freccia: #1B2A4A (diventa bianco su hover)

---

### SEZIONE 2 — IL MERCATO

**Sfondo:** #FFFFFF

**Titolo:** `IL MERCATO`
**Sottotitolo:** *"Bisogni reali, soluzioni parziali."*

**Layout 3 blocchi verticali:**

**Blocco A — Il problema**
Titolo colonna: COSA MANCA
- Insight dispersi: fonti, note, transcript, watchlist vivono in flussi separati. Convergere in un output decisionale chiaro è difficile.
- Workflow lenti: parte rilevante del lavoro di ricerca resta manuale, poco standardizzata.
- Competenze quant inaccessibili: i team small/mid non hanno scala per costruire internamente.

**Blocco B — Cosa offre il mercato**
Titolo colonna: L'OFFERTA ESISTENTE
Lista compatta:
- Bloomberg/Refinitiv/FactSet — dati standard, costo elevato (~$24k/anno), personalizzazione limitata
- Axyon, MDOTM, RavenPack — segnali pronti, black-box, non customizzabili
- Exabel, Boosted.ai — workbench quant, richiedono team interno strutturato e budget significativi
- Custom indices — accessibili solo a realtà con masse rilevanti

**Blocco C — Perché non bastano**
Titolo colonna: I FRENI ALL'ADOZIONE
- Black-box: il 65% (survey Assogestioni 2025) cita la spiegabilità come ostacolo n.1
- Customizzazione: richiede costi elevati e competenze interne
- Lock-in: timore di dipendere da un vendor per una fase critica del processo
- Co-sviluppo assente: il mercato vende output, non costruisce insieme al cliente

**Download block** (sotto i 3 blocchi):
Titolo sezione download: APPROFONDIMENTI DI MERCATO
Due card download affiancate:
- 📄 Ricerca di mercato — insight e segnali quantitativi (Italia)
- 📄 Ricerca di mercato — provider dati USA ed Europa

---

### SEZIONE 3 — VALUE PROPOSITION

**Sfondo:** #F7F6F3

**Titolo:** `VALUE PROPOSITION`
**Sottotitolo:** *"Decision support quantitativo su misura."*

**Testo introduttivo:**
Notung aiuta SGR, SIM e family office a trasformare una domanda di investimento in un segnale quantitativo proprietario, validato e immediatamente utilizzabile nel processo decisionale. Non vende una piattaforma standard né un feed chiuso: costruisce con il cliente il modello, lo implementa in una soluzione stand-alone e lo rilascia come asset proprietario del cliente.

**Griglia 2x2 — Offerta commerciale:**

Card 1 — CUSTOM INDICES
Progettazione e co-creazione di indici proprietari. L'IP resta al cliente.

Card 2 — CUSTOM RISK MODELS
Modelli di rischio customizzati su engine/dati del cliente. Anche as-a-service.

Card 3 — PIATTAFORME ALTERNATIVE DATA
Analisi di testi, immagini, dati non strutturati integrati nel processo d'investimento.

Card 4 — SIGNAL DISCOVERY
Ricerca di pattern statisticamente robusti su universo titoli definito dal cliente.

**Stile card offerta:**
- Bordo-left 3px solid #1B2A4A
- Padding 20px 24px
- Sfondo #FFFFFF
- Titolo: CoolVetica 11px maiuscolo, colore #1B2A4A
- Corpo: EB Garamond 15px

**Poi: Selling points in lista orizzontale (5 elementi)**
Ognuno: icona Lucide lineare + label CoolVetica + frase EB Garamond

1. 🔒 ASSET PROPRIETARIO — Codice, logica e documentazione trasferiti in-house. Nessun lock-in.
2. 👁 CO-SVILUPPO — Il cliente partecipa alla costruzione. Nessuna black-box.
3. ⚡ RAPIDITÀ — Da firma a sistema live: 10-15 settimane.
4. 📊 OUTPUT AZIONABILE — Segnali presentabili in comitato investimenti con test e documentazione.
5. 🔗 INTEGRAZIONE DATI FLESSIBILE — Fonti open, vendor esistenti del cliente, alternative data.

---

### SEZIONE 4 — PUNTI DI FORZA

**Sfondo:** #FFFFFF

**Titolo:** `PUNTI DI FORZA`

**Layout: 3 colonne x 2 righe (6 blocchi)**

1. **RAPIDITÀ** — Soluzione browser-based, stand-alone. Nessuna integrazione con sistemi proprietari richiesta. Operativa in settimane.

2. **SICUREZZA STATISTICA** — Modelli progettati con disciplina: separazione in-sample/out-of-sample, test statistici, anti-overfitting, registry tracciabile.

3. **NO LOCK-IN** — Il sistema gira nel vostro Azure. Il codice è vostro dalla prima riga. Se Notung chiudesse domani, il sistema continua a girare.

4. **TRASPARENZA** — Output leggibili, documentabili, difendibili in comitato. Il cliente capisce cosa compra perché ha partecipato a costruirlo.

5. **PERSONALIZZAZIONE** — Ogni progetto nasce da una domanda specifica del cliente. Nessun prodotto uguale per tutti. Integrazione con dati custom (Excel, PDF, Word) del personale.

6. **COMPLIANCE DORA** — Il modello client-hosted riduce sostanzialmente il profilo di rischio DORA. La soluzione viene trasferita in-house: nessun ICT third-party provider critico da registrare.

**Download block:**
Card download singola:
- 📄 Ricerca sull'acquistabilità di una boutique di decision support quant

---

### SEZIONE 5 — COME SI COSTRUISCE UNA PIATTAFORMA

**Sfondo:** #F7F6F3

**Titolo:** `COME SI COSTRUISCE`
**Sottotitolo:** *"Dalla domanda di investimento al sistema live."*

**Timeline verticale — 5 fasi:**

Ogni fase: numero grande CoolVetica (64px, colore #E8E4DC) + titolo + durata + descrizione

```
① DISEGNO DEL PROGETTO          1–2 settimane
  Si trasforma la domanda di investimento in un'ipotesi testabile.
  Dataset, metriche di successo e criteri di validazione concordati per iscritto.

② RICERCA E PROTOTIPO            3–5 settimane
  Sviluppo del modello in locale. Backtest rigoroso con test statistici.
  Il decision memo è il gate: se il segnale non regge, la Fase 3 non parte.
  ⚠ Il cliente non paga la Fase 3 se la Fase 2 non porta risultati.

③ DEPLOYMENT                     4–6 settimane
  Il prototipo diventa un sistema live su Azure del cliente.
  Motore automatico, magazzino dati, dashboard web.
  Il codice è proprietà del cliente dalla prima riga.

④ INTEGRAZIONE API               1–3 settimane
  Connessione ai vendor dati del cliente (Bloomberg, Refinitiv, FactSet).
  Tempi dipendono dal provider — Bloomberg richiede assessment separato.

⑤ MONITORING & EVOLUTION         Continuativo
  Il segnale viene monitorato per drift.
  Nuove release gestite con processo formale.
```

Il numero grande in background crea gerarchia visiva. Linea verticale sottile (1px, #E8E4DC) collega le fasi.

**Download block:**
- 📄 Notung Manuale Operativo (DOCX)

---

### SEZIONE 6 — DATI & ARCHITETTURA

**Sfondo:** #FFFFFF

**Titolo:** `DATI & ARCHITETTURA`
**Sottotitolo:** *"Il dato vive nel perimetro licenze del cliente."*

**2 colonne:**

Colonna sinistra — MODELLO BYOD
Testo: Notung non rivende dati grezzi. Consegna software, connettori e segnali derivati. Il dato vive nel perimetro licenze del cliente — nessun obbligo di redistribuzione.

Tabella compatta provider:
| Provider | Integrazione | Complessità |
|---|---|---|
| Bloomberg B-PIPE | SDK proprietario (blpapi) | Alta — richiede IT |
| LSEG / Refinitiv | REST API moderna | Bassa |
| FactSet | REST API documentata | Bassa–media |
| S&P Capital IQ | REST API (Swagger) | Bassa–media |
| SIX Financial | Feed SFTP / API enterprise | Media |

Nota: *Bloomberg è un caso a parte — non è una REST API. Richiede terminale fisico attivo. Coinvolgimento IT obbligatorio dal giorno zero.*

Colonna destra — STACK AZURE
Lista verticale con icone lineari:
- Azure Function → motore automatico giornaliero
- Blob Storage + Parquet → archivio immutabile dati raw, point-in-time
- Azure SQL Database → storico segnali con forward return reale
- App Service → dashboard Streamlit/Dash via browser
- Key Vault → credenziali mai nel codice, mai visibili a Notung
- GitHub (CI/CD) → tre ambienti: locale → staging → produzione

**Download block (2 card):**
- 📄 Integrazione Data provider terzi (DOCX)
- 📄 Ricerca di mercato — Data provider SGR e SIM (PDF)

---

### SEZIONE 7 — DORA Q&A

**Sfondo:** #F7F6F3

**Titolo:** `DORA`
**Sottotitolo:** *"Le domande che ogni compliance officer fa."*

**Accordion espandibile — 7 domande/risposte:**

Q1: Siete una piccola realtà senza certificazioni. Come vi inseriamo nel registro fornitori ICT?
R: Non siamo un fornitore ICT nel senso che DORA intende. Non ospitiamo i vostri dati, non gestiamo infrastrutture critiche, non eroghiamo un servizio continuativo in cloud. Il sistema gira nel vostro Azure, con le vostre credenziali, sotto il vostro controllo. Il nostro ruolo è paragonabile a quello di un consulente che vi ha scritto del codice — non a quello di un SaaS da cui dipendete operativamente.

Q2: E se Notung chiudesse domani?
R: È esattamente il punto su cui siamo strutturalmente più forti di qualsiasi alternativa SaaS. Se chiudessimo domani: il sistema continua a girare nel vostro Azure, il codice è vostro, la documentazione è vostra, i dati sono nel vostro storage. Non dipendete da noi per nessuna funzione operativa quotidiana.

Q3: Non avete ISO 27001 né SOC 2. Come gestiamo la due diligence?
R: Abbiamo qualcosa di meglio di una certificazione: un'architettura che riduce il perimetro di rischio. I vostri dati non ci passano mai — restano nel vostro Azure. Le credenziali le caricate voi nel Key Vault — noi non le vediamo mai in chiaro. Il nostro accesso è limitato, tracciato tramite Azure AD e revocabile in qualsiasi momento.

Q4: Come gestiamo i diritti di audit previsti da DORA?
R: Il codice è vostro — potete auditarlo quando volete. Il sistema gira nel vostro Azure — il vostro IT ha accesso completo a log, dati, infrastruttura. L'audit right DORA serve per ispezionare quello che il fornitore fa con i vostri dati nel suo ambiente. Nel nostro modello quell'ambiente è il vostro.

Q5: Avete un piano BCP?
R: Il BCP per un sistema Notung coincide con il fatto che il sistema non dipende da Notung per girare. Non c'è un servizio Notung da mantenere attivo — c'è il vostro Azure, con i propri SLA garantiti da Microsoft (99.9%+ per App Service e Azure Function).

Q6: DORA richiede SLA contrattuali. Cosa garantite?
R: SLA di supporto coerenti con le vostre esigenze di processo. Exit policy formale con consegna di codice, documentazione e dati entro 30 giorni.

Q7: Usate librerie open source. Come gestiamo il rischio vulnerabilità?
R: Le librerie usate (pandas, numpy, plotly, azure-sdk) sono standard industriali usati da milioni di applicazioni enterprise, incluse banche e asset manager. Il codice è nel vostro GitHub — il vostro IT può eseguire vulnerability scan quando vuole. Aggiornamenti delle dipendenze gestiti ad ogni release e documentati nel CHANGELOG.

**Stile accordion:**
- Domanda: CoolVetica 13px maiuscolo, border-bottom 1px #E8E4DC, padding 16px 0
- Risposta: EB Garamond 16px, sfondo #FFFFFF, padding 16px 24px, border-left 2px #1B2A4A
- Freccia: ruota 90° su apertura

---

### SEZIONE 8 — Q&A GENERALI

**Sfondo:** #FFFFFF

**Titolo:** `DOMANDE FREQUENTI`

**3 colonne per categoria:**

**Colonna 1 — COMMERCIALE**

Q: Non capisco cosa stai vendendo. Sei un consulente o un software vendor?
R: Sono un capability builder. Costruisco un modello quantitativo validato, lo deplojo nel vostro Azure e ve lo consegno come asset proprietario con codice, documentazione e monitoring. Il deliverable non è un report — è un sistema che gira ogni mattina e che resta vostro.

Q: Il mercato ha già Axyon, MDOTM, Exabel. Perché venire da te?
R: Quei vendor vendono output confezionati su universi predefiniti con motori che non controllate. Io costruisco il segnale con voi, su vostro universo, e ve lo consegno con tutto: codice, test statistici, documentazione. Quando il comitato chiede "come funziona?", avete una risposta.

**Colonna 2 — BUDGET & ROI**

Q: Non ho budget per "ricerca del segnale".
R: Non la mettete a budget come ricerca — la mettete come acquisto di una capability analitica interna. Il benchmark sono i custom indices: stesso modello — comprate un asset governato, non un abbonamento a un servizio esterno.

Q: Come dimostri che il segnale genera valore reale?
R: Con numeri e processo: forward return 2.6% vs baseline 0.8%, win rate 63.4%, parametri scelti prima di guardare i risultati, separazione in-sample/out-of-sample, t-test. È quello che portate in comitato investimenti — non una promessa, una metodologia difendibile.

**Colonna 3 — RISCHIO EXECUTION**

Q: Progetti bespoke hanno cicli lunghi e outcome incerti.
R: Gate espliciti: Fase 1 (1-2 settimane) definisce l'ipotesi, Fase 2 (3-5 settimane) produce un decision memo con verdetto chiaro. Se il segnale non regge, ci fermiamo — non pagate la Fase 3.

Q: Il backtest funziona, ma poi live no. Chi si prende la responsabilità?
R: Il backtest è una prova statistica, non una garanzia — e questo sta nel contratto. Garantiamo rigore metodologico e monitoring continuativo per rilevare drift. Stessa logica dei risk model provider: Axioma non garantisce alpha, garantisce un modello governato e mantenuto.

---

### SEZIONE 9 — FOOTER

**Sfondo:** #1B2A4A (Blu notte — come hero)
**Contenuto centrato:**

```
NOTUNG
Signal over noise.

[spazio]

Per informazioni e proposte di collaborazione scrivere a:
[indirizzo email — da aggiungere manualmente]

[spazio]

© 2025 Notung. Tutti i diritti riservati.
```

- NOTUNG: CoolVetica 48px bianco
- Signal over noise.: EB Garamond corsivo 18px, #B0BDD4
- Testo contatti: EB Garamond 15px, #B0BDD4

---

## IMPLEMENTAZIONE TECNICA — NOTE SPECIFICHE STREAMLIT

### Injection CSS
Usare `st.markdown("""<style>...[CSS]...</style>""", unsafe_allow_html=True)` in cima all'app per:
- Importare Google Fonts (CoolVetica via @font-face o alternativa, EB Garamond da Google Fonts)
- Override stili Streamlit (nascondere header default, menu, footer)
- Definire classi custom per sezioni, card, download block
- Stili hover per card POC

### Nascondere elementi Streamlit di default
```css
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp > header {display: none;}
```

### Download button
Usare `st.download_button()` di Streamlit per i file in `/assets/`.
Stile: sovrascrivere con CSS per far sembrare le card di download e non bottoni generici.

Alternativa più controllata: leggere il file con `open()`, passare a `st.download_button()` con label custom, icon, e CSS iniettato che trasforma il bottone in card.

### Navigazione sezioni
Usare anchor HTML con `<div id="sezione-x">` e link `<a href="#sezione-x">` nella nav.
La nav sticky si ottiene con CSS `position: sticky; top: 0; z-index: 999`.

### Accordion DORA
Usare `st.expander()` di Streamlit per le domande DORA e Q&A generali.
Oppure implementare accordion puro HTML/CSS via `st.markdown(unsafe_allow_html=True)` per controllo totale sullo stile.

### Layout colonne
Usare `st.columns()` per i layout a 2-3 colonne.

### CoolVetica Font
CoolVetica non è su Google Fonts. Due opzioni:
1. Scaricare il file .ttf e includerlo nella cartella `/assets/fonts/`, poi caricare via @font-face
2. Usare come alternativa "Barlow Condensed" da Google Fonts (simile per impatto visivo, uppercase, tracking)
   → `@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap');`

**Raccomandazione:** Usare Barlow Condensed 600 in maiuscolo come sostituto CoolVetica — stessa energia visiva, disponibile su Google Fonts, zero problemi di licensing.

---

## STILE CARD DOWNLOAD — SPECIFICHE

```css
.download-card {
  border: 1px solid #1B2A4A;
  padding: 20px 24px;
  background: #FFFFFF;
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  transition: background 200ms, color 200ms;
}
.download-card:hover {
  background: #1B2A4A;
  color: #FFFFFF;
}
.download-card .doc-type {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #4A4A52;
}
.download-card .doc-name {
  font-family: 'EB Garamond', serif;
  font-size: 16px;
  color: #1C1C1E;
}
.download-card .arrow {
  margin-left: auto;
  color: #1B2A4A;
}
```

---

## MAPPA DOWNLOAD → FILE

| Sezione | Label visualizzata | File |
|---|---|---|
| Mercato | Ricerca — insight e segnali quantitativi (Italia) | `Ricerca di mercato sul mercato italiano di insight e segnali quantitativi.pdf` |
| Mercato | Ricerca — provider dati USA ed Europa | `Ricerca di mercato sui provider dati per USA ed Europa.pdf` |
| Punti di forza | Ricerca — acquistabilità boutique decision support | `Ricerca di mercato sull'acquistabilità di una boutique di decision support quant.pdf` |
| Come si costruisce | Notung Manuale Operativo | `Notung Manuale Operativo.docx` |
| Dati & Architettura | Integrazione Data provider terzi | `Integrazione Data provider terzi.docx` |
| Dati & Architettura | Ricerca — Data provider SGR e SIM | `Ricerca di mercato Data provider SGR e SIM.pdf` |
| (opzionale in footer) | Notung Guida Tecnica | `Notung Guida Tecnica.docx` |

---

## PRIORITÀ DI SVILUPPO

1. **Prima cosa:** struttura HTML/CSS corretta con brand identity (font, colori, sezioni)
2. **Seconda cosa:** contenuti testuali completi in ogni sezione
3. **Terza cosa:** download button funzionanti per ogni file
4. **Quarta cosa:** link POC cliccabili nella sezione 1
5. **Quinta cosa:** nav sticky funzionante con scroll
6. **Sesta cosa:** accordion DORA e Q&A
7. **Rifinitura finale:** hover states, spaziatura, ritmo visivo
