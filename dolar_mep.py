import requests
from bs4 import BeautifulSoup

def obtener_dolar_mep():
    url = "https://www.dolarhoy.com/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar todos los bloques de cotización
        bloques = soup.find_all("div", class_="tile is-parent")

        for bloque in bloques:
            titulo = bloque.find("a")
            if titulo and "dólar mep" in titulo.text.lower():
                valor = bloque.find("div", class_="value")
                if valor:
                    numero = valor.text.strip().replace("$", "").replace(".", "").replace(",", ".")
                    return float(numero)
    except Exception as e:
        print("Error al obtener Dólar MEP:", e)

    return None