from bs4 import BeautifulSoup
import logging

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
def extract():
    # url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
    reqs = open("./rki_daten/output.txt")

    soup = BeautifulSoup(reqs, 'html.parser')

    with open(r'./rki_daten/urls_total.txt', 'w') as fp:
        for link in soup.find_all('a'):
            spe_url = link.get('href')
            fp.write("%s\n" % spe_url)


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    extract()
    logging.info("urls_total.txt wurde aktualisiert.")
