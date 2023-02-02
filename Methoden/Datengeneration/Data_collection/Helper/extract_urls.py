from bs4 import BeautifulSoup

import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## schreibt die in output gespeicherten Links in URLs um

# Benötigt:
## Datei: "output.txt"

# Gibt zurück:
## Datei: "urls_total.txt"

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
