import logging
import urllib.request

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Data_collection über das Module "aktualitaet.py" auf
## Aktualität und sortiert über "sort_meld.py" nach Meldedatum. Danach wird das Startdatum sowie Enddatum bestimmt und
## die Zahl der resultierenden Fälle pro Tag als Graph ausgegeben.

# Benötigt:
## "aufruf_lk.py"
## "aktualitaet.py"
## "sort_meld.py"
## "datumseingabe.py"

# Gibt zurück:
## 2d-Graph mit der x = Datum und Y = Anzahl Fälle

# ----------------------------------------------------------------------------------------------------------------------

def download(next_url):
    urllib.request.urlretrieve(next_url, "./rki_daten/date.xz")
    return next_url


def main(next_url):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    download(next_url)
    logging.info(f"Die URL {next_url} wurde erfolgreich herunter geladen.")
    return next_url
