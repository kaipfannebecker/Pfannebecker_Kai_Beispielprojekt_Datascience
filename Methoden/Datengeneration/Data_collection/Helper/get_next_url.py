import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## liest die erste Zeile aus urls_unique.txt ein und gibt diese als Variable next_url aus

# Benötigt:
## Datei: "urls_unique.txt"

# Gibt zurück:
## Variable: "next_url"

# ----------------------------------------------------------------------------------------------------------------------


def get_next_url():
    urls_unique = open("./rki_daten/urls_unique.txt", "r")
    next_url = urls_unique.readline()
    return next_url


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    next_url = get_next_url()
    logging.info(f"{next_url} wurde ausgelesen und übergeben.")
    return next_url
