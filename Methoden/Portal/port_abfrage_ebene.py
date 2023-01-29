import sys
import logging

from Methoden.Auswertung.Helper import aktualitaet

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


def abfrage_variablen_ebene():
    # Abfrage Ebene:
    ebene = eval(input(
        "Auf welcher Ebene möchten Sie die Data_collection betrachten:\n"
        "1) Landkreise\n"
        "2) Bundesländer\n"
        "3) Bundesgebiet\n"
        "4) zurück zur vorherigen Auswahl\n"
        "5) Abbruch\n"
        " "
    ))

    if ebene == 4:
        sys.exit()  # to change

    if ebene == 5:
        sys.exit()
    return ebene


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

    ebene = abfrage_variablen_ebene()

    return ebene

    # ----------------------------------------------------------------------------------------------------------------------