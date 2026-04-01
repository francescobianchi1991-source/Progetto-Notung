import streamlit as st

st.set_page_config(
    page_title="Notung — Signal over noise.",
    page_icon="◈",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap');

/* App background */
.stApp { background-color: #F7F6F3; }
.block-container { padding: 2rem 3rem; max-width: 900px; }

/* Sidebar */
[data-testid="stSidebar"] { background-color: #1B2A4A; }
[data-testid="stSidebar"] * { color: #FFFFFF !important; }
[data-testid="stSidebarNav"] a { font-family: 'Barlow Condensed', sans-serif; font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase; }

/* Titoli */
h1 { font-family: 'Barlow Condensed', sans-serif !important; font-weight: 600 !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; color: #1C1C1E !important; }
h2 { font-family: 'Barlow Condensed', sans-serif !important; font-weight: 500 !important; text-transform: uppercase !important; letter-spacing: 0.04em !important; color: #1C1C1E !important; }
h3 { font-family: 'Barlow Condensed', sans-serif !important; color: #1B2A4A !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; }

/* Corpo testo */
p, li, .stMarkdown { font-family: 'EB Garamond', serif !important; font-size: 17px !important; line-height: 1.65 !important; color: #1C1C1E !important; }

/* Download button */
.stDownloadButton button {
  background: #FFFFFF !important;
  color: #1C1C1E !important;
  border: 1px solid #1B2A4A !important;
  border-radius: 0 !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 12px !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  padding: 12px 20px !important;
  width: 100% !important;
}
.stDownloadButton button:hover {
  background: #1B2A4A !important;
  color: #FFFFFF !important;
}

/* Link button (POC demo) */
.stLinkButton a {
  background: transparent !important;
  color: #1B2A4A !important;
  border: 1px solid #1B2A4A !important;
  border-radius: 0 !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 12px !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
}
.stLinkButton a:hover {
  background: #1B2A4A !important;
  color: #FFFFFF !important;
}

/* Expander (DORA accordion) */
.stExpander { border: 1px solid #E8E4DC !important; border-radius: 0 !important; }
.stExpander summary { font-family: 'Barlow Condensed', sans-serif !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; font-size: 14px !important; }

/* Nasconde elementi Streamlit */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("# NOTUNG")
st.sidebar.markdown("*Signal over noise.*")
st.sidebar.markdown("---")

st.sidebar.markdown("---")
st.sidebar.markdown("*© 2025 Notung*")
