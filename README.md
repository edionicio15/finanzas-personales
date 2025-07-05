# 📊 Gestor de Finanzas Personales

Esta app te permite gestionar ingresos, gastos, recordatorios y consultar el dólar MEP desde una interfaz web simple y visual (usando Streamlit).

---

## ✅ Funcionalidades principales

- Registro manual de ingresos y gastos
- Conversión automática de USD a ARS con dólar MEP en tiempo real
- Dashboard con métricas, gráficos y evolución mensual
- Generación de recordatorios en formato .ics (para Google Calendar u Outlook)
- Soporte para múltiples cuentas y tarjetas
- Selección de **categorías y cuentas desde un archivo editable (`CATEGORIAS.xlsx`)**

---

## 🆕 NUEVO: Categorías y Cuentas dinámicas

- Las listas desplegables de "Categoría" y "Cuenta/Tarjeta" se cargan automáticamente desde el archivo:
  ```
  CATEGORIAS.xlsx
  ```
- También podés ingresar una **categoría o cuenta nueva manualmente** (opción "Otra...").

---

## 📂 Estructura esperada del archivo `CATEGORIAS.xlsx`

Debe tener una hoja (por ejemplo, `Hoja1`) con estas columnas:

| CATEGORIA       | CUENTA     |
|------------------|------------|
| SALARIO          | GALICIA    |
| HONORARIOS       | BRUBANK    |
| CUOTA ESCUELA    | MACRO      |
| ...              | ...        |

---

## 📦 Requisitos

- Python 3.8 o superior

### Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Cómo ejecutar la app

1. Cloná o descomprimí este repositorio.
2. Ejecutá:

```bash
streamlit run app.py
```

3. Usá el menú lateral para navegar entre:
   - Dashboard
   - Ingreso manual
   - Cotización dólar MEP
   - Recordatorios

---

## 🌍 Publicación en Streamlit Cloud

1. Subí este repo a GitHub.
2. Ingresá a [streamlit.io/cloud](https://streamlit.io/cloud).
3. Vinculá tu cuenta de GitHub.
4. Deploy → seleccioná `app.py` como archivo principal.

---

¡Listo! Ahora tenés una herramienta visual y flexible para controlar tus finanzas 💼📈