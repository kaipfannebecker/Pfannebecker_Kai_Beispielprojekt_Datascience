import sys
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
## Weiteren Module zur Darstellung

# ----------------------------------------------------------------------------------------------------------------------


def abfrage_variablen_datensatz():
    # Abgefragter Datensatz:
    datensatz = eval(input(
        "Welche Data_collection möchten Sie angezeigt haben:\n"
        "1) Neue Fälle\n"
        "2) Neue Genesene\n"
        "3) Neue Todesfälle\n"
        "4) zurück zur vorherigen Auswahl\n"
        "5) Abbruch\n"
        " "
    ))

    if datensatz == 4:
        sys.exit()  # to change

    if datensatz == 5:
        sys.exit()

    return datensatz

# ----------------------------------------------------------------------------------------------------------------------


def main():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    datensatz = abfrage_variablen_datensatz()

    return datensatz

    # ----------------------------------------------------------------------------------------------------------------------