import streamlit as st
import pandas as pd
from datetime import datetime
import os
from dolar_mep import obtener_dolar_mep

def app():
    st.title("📝 Ingreso manual de gasto o ingreso")

    with st.form("form_ingreso"):
        fecha = st.date_input("Fecha", datetime.today())
        tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
        categoria = st.text_input("Categoría")
        monto = st.number_input("Monto", min_value=0.0)
        moneda = st.selectbox("Moneda", ["ARS", "USD"])
        cuenta = st.text_input("Cuenta/Tarjeta")
        observaciones = st.text_area("Observaciones")

        enviar = st.form_submit_button("Guardar")

        if enviar:
            if moneda == "USD":
                dolar_mep = obtener_dolar_mep()
                if dolar_mep:
                    monto_ars = monto * dolar_mep
                    st.info(f"💵 Convertido a ARS: ${monto_ars:.2f} (Dólar MEP ${dolar_mep:.2f})")
                else:
                    st.warning("⚠️ No se pudo obtener cotización MEP, guardando monto sin conversión.")
                    monto_ars = monto
            else:
                monto_ars = monto

            nuevo = {
                "Fecha": fecha,
                "Tipo": tipo,
                "Categoría": categoria,
                "Monto": monto_ars,
                "Moneda": moneda,
                "Cuenta/Tarjeta": cuenta,
                "Observaciones": observaciones
            }

            archivo_csv = "datos_financieros.csv"
            if os.path.exists(archivo_csv):
                df_existente = pd.read_csv(archivo_csv, parse_dates=["Fecha"])
                df_nuevo = pd.DataFrame([nuevo])
                df_final = pd.concat([df_existente, df_nuevo], ignore_index=True)
            else:
                df_final = pd.DataFrame([nuevo])

            df_final.to_csv(archivo_csv, index=False)
            st.success("✅ Registro guardado exitosamente.")