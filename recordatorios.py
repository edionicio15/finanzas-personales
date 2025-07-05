from ics import Calendar, Event
from datetime import datetime, timedelta

def crear_recordatorios(recordatorios, archivo_salida="recordatorios.ics"):
    calendario = Calendar()
    for r in recordatorios:
        evento = Event()
        evento.name = r["titulo"]
        evento.begin = r["fecha"].strftime("%Y-%m-%d")
        evento.description = r.get("descripcion", "")
        evento.make_all_day()
        calendario.events.add(evento)

    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.writelines(calendario)