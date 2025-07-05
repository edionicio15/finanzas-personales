import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("📊 Dashboard financiero")

    try:
        df = pd.read_csv("datos_financieros.csv", parse_dates=["Fecha"])
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo de datos. Cargá algunos movimientos primero.")
        return

    # Filtros
    st.sidebar.subheader("Filtros")
    tipo = st.sidebar.multiselect("Tipo de movimiento", options=df["Tipo"].unique(), default=list(df["Tipo"].unique()))
    cuenta = st.sidebar.multiselect("Cuenta/Tarjeta", options=df["Cuenta/Tarjeta"].unique(), default=list(df["Cuenta/Tarjeta"].unique()))
    moneda = st.sidebar.multiselect("Moneda", options=df["Moneda"].unique(), default=list(df["Moneda"].unique()))

    df_filtrado = df[
        (df["Tipo"].isin(tipo)) &
        (df["Cuenta/Tarjeta"].isin(cuenta)) &
        (df["Moneda"].isin(moneda))
    ]

    if df_filtrado.empty:
        st.info("No hay datos con los filtros seleccionados.")
        return

    # Métricas
    total_ingresos = df_filtrado[df_filtrado["Tipo"] == "Ingreso"]["Monto"].sum()
    total_gastos = df_filtrado[df_filtrado["Tipo"] == "Gasto"]["Monto"].sum()
    saldo = total_ingresos - total_gastos

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Ingresos", f"${total_ingresos:,.2f}")
    col2.metric("💸 Gastos", f"${total_gastos:,.2f}")
    col3.metric("🧮 Saldo", f"${saldo:,.2f}")

    # Gráfico por categoría
    st.subheader("Distribución por Categoría")
    df_cat = df_filtrado[df_filtrado["Tipo"] == "Gasto"].groupby("Categoría")["Monto"].sum().reset_index()
    if not df_cat.empty:
        fig = px.pie(df_cat, names="Categoría", values="Monto", title="Gastos por Categoría")
        st.plotly_chart(fig)
    else:
        st.info("No hay gastos para mostrar.")

    # Evolución en el tiempo
    st.subheader("Evolución mensual")
    df_filtrado["Mes"] = df_filtrado["Fecha"].dt.to_period("M").astype(str)
    df_mes = df_filtrado.groupby(["Mes", "Tipo"])["Monto"].sum().reset_index()
    fig2 = px.bar(df_mes, x="Mes", y="Monto", color="Tipo", barmode="group", title="Ingresos y Gastos por Mes")
    st.plotly_chart(fig2)