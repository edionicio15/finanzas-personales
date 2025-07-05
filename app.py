import streamlit as st
import pandas as pd
from Scripts.finanzas_personales.ingreso_manual import app as ingreso_app
from Scripts.finanzas_personales.dolar_mep import obtener_dolar_mep
from Scripts.finanzas_personales.dashboard import app as dashboard_app
from Scripts.finanzas_personales.vencimientos import app as vencimientos_app

st.set_page_config(page_title="Gestor de Finanzas", layout="centered")

# ---------- Título Principal ---------- #
st.title("💼 Gestor de Finanzas Personales")

# ---------- Menú ---------- #
menu = st.sidebar.selectbox(
    "Elegí una opción",
    ["Dashboard", "Ingreso manual", "Ver Dólar MEP", "Generar recordatorios"]
)

# ---------- Funcionalidad ---------- #
if menu == "Ingreso manual":
    ingreso_app()

elif menu == "Ver Dólar MEP":
    st.header("💵 Cotización actual del Dólar MEP")
    dolar = obtener_dolar_mep()
    if dolar:
        st.success(f"El valor actual del Dólar MEP es: ${dolar:.2f} ARS")
    else:
        st.error("No se pudo obtener la cotización actual.")

elif menu == "Dashboard":
    dashboard_app()

elif menu == "Generar recordatorios":
    vencimientos_app()