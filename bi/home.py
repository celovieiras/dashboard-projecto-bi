import streamlit.components.v1 as comp
import streamlit as st

st.set_page_config(page_title="Dashboard Cosméticos", page_icon="📊",layout="wide")
st.title("Panel de control del mercado de cosmetología")
comp.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDgyZTVhMzQtZGUzYi00NGU2LTg0ODctOGJiMTNjNDdjMTAzIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9", height=720, width=1280)