import requests

import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## liest vorhandene URLs aus und spreichert diese in output.txt"

# Benötigt:
## -

# Gibt zurück:
## output.txt"

# ----------------------------------------------------------------------------------------------------------------------


def curl():
    url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
    reqs = requests.get(url)
    whole_download = reqs.text
    with open("./rki_daten/output.txt", "w") as text_file:
        print(whole_download, file=text_file)


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    curl()
    logging.info("output.txt wurde aktualisiert.")
