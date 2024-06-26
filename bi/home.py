import streamlit.components.v1 as comp
import streamlit as st

st.set_page_config(page_title="Dashboard Cosméticos", page_icon="📊",layout="wide")
st.title("Panel de control del mercado de cosmetología")
comp.iframe("https://app.powerbi.com/view?r=eyJrIjoiNWE3MTc2MzUtOWFhZS00MWE4LTkxODMtYWIwMWM0YmE4NWQ2IiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9&pageName=68e2a99b952ab9705354", height=720, width=1280)