# 📊 Gestor de Finanzas Personales

Esta app te permite gestionar tus ingresos, gastos, vencimientos y consultar el dólar MEP desde una interfaz simple usando Streamlit.

## ✅ Funcionalidades principales

- Registro manual de ingresos y gastos (ARS o USD)
- Conversión automática de USD a ARS con cotización MEP en tiempo real
- Dashboard con métricas y gráficos
- Generación de recordatorios en archivo .ics para calendario
- Soporte para múltiples cuentas/tarjetas

---

## 🚀 Requisitos

- Python 3.8 o superior

### Instalación de dependencias

```bash
pip install streamlit pandas matplotlib plotly openpyxl requests beautifulsoup4 ics
```

---

## ▶️ Cómo ejecutar la app

1. Cloná o descomprimí el contenido del ZIP.
2. Desde la carpeta `finanzas_personales`, ejecutá:

```bash
streamlit run app.py
```

3. Usá el menú lateral para acceder a:
   - Dashboard
   - Ingreso manual
   - Consulta de dólar MEP
   - Generación de recordatorios

---

## 📅 Recordatorios

Usá `vencimientos_template.csv` como base para tus eventos de pago. Luego cargalo desde la sección **"Generar recordatorios"** para obtener un archivo `.ics` importable en Google Calendar o Outlook.

---

## 📂 Archivos incluidos

- `app.py`
- `ingreso_manual.py`
- `dashboard.py`
- `dolar_mep.py`
- `vencimientos.py`
- `vencimientos_template.csv`

---

¡Gracias por usar esta app! 💼💡