import streamlit as st
import pandas as pd
from ics import Calendar, Event
from datetime import datetime

def app():
    st.title("📅 Generador de Recordatorios")

    archivo = st.file_uploader("Subí tu archivo de vencimientos (CSV)", type=["csv"])

    if archivo:
        try:
            df = pd.read_csv(archivo, parse_dates=["Fecha"])
            st.success("✅ Archivo cargado correctamente. Mostrando datos:")
            st.dataframe(df)

            cal = Calendar()
            for _, row in df.iterrows():
                evento = Event()
                evento.name = row["Titulo"]
                evento.begin = row["Fecha"].strftime("%Y-%m-%d")
                evento.make_all_day()
                evento.description = row.get("Descripcion", "")
                cal.events.add(evento)

            with open("vencimientos_personales.ics", "w", encoding="utf-8") as f:
                f.writelines(cal)

            with open("vencimientos_personales.ics", "rb") as f:
                st.download_button("📥 Descargar archivo .ics para tu calendario", f, file_name="vencimientos.ics")

        except Exception as e:
            st.error(f"❌ Error al procesar el archivo: {e}")