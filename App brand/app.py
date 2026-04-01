import streamlit as st
from utils import inject_css, sidebar_brand

st.set_page_config(
    page_title="Notung — Signal over noise.",
    page_icon="◈",
    layout="wide",
)

inject_css()
sidebar_brand()

st.title("NOTUNG")
st.markdown("*Signal over noise.*")
