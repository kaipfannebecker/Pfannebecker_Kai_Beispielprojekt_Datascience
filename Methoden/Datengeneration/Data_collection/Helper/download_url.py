import urllib.request

import logging


# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## läd den Inhalt der URL in date.xz

# Benötigt:
## Variable: next_url

# Gibt zurück:
## Datei: date.xz

# ----------------------------------------------------------------------------------------------------------------------


def download(next_url):
    urllib.request.urlretrieve(next_url, "./rki_daten/date.xz")


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
