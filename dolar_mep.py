import requests
from bs4 import BeautifulSoup

def obtener_dolar_mep():
    url = "https://dolarhoy.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        div = soup.find("a", href="/cotizaciondolar-mep")
        if div:
            texto = div.find("div", class_="val").text.strip().replace("$", "").replace(",", ".")
            return float(texto)
    except Exception as e:
        print("Error al obtener Dólar MEP:", e)
    return None