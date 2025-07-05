import pandas as pd

def cargar_resumen_excel(ruta_archivo, nombre_cuenta):
    df = pd.read_excel(ruta_archivo)
    df = df.rename(columns=lambda x: x.strip().lower())
    df["cuenta"] = nombre_cuenta
    df["tipo"] = "Gasto"
    df["moneda"] = df.get("moneda", "ARS")
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["observaciones"] = df.get("detalle", "")
    return df[["fecha", "tipo", "detalle", "importe", "moneda", "cuenta", "observaciones"]]