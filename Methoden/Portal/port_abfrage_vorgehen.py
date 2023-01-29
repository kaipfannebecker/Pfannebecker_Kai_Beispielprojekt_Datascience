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


def abfrage_vorgehen():
    vorgehen_1 = eval(input(
        "Möchten Sie die Data_collection zuerst aktualisieren oder die vorhandenen Data_collection direkt auswerten? \n"
        "1) aktualisieren\n"
        "2) auswerten\n"
        "3) Abbruch\n"
        " "
    ))

    if vorgehen_1 == 1:
        while True:
            aktualitaet.main()
            weitere_akt = eval(input(
                "Möchten Sie eine weitere Aktualisierung vornehmen?\n"
                "1) Ja\n"
                "2) Nein\n"
                "3) Abbruch\n"
                "")
            )
            if weitere_akt == 1:
                pass

            if weitere_akt == 2:
                break

            if weitere_akt == 3:
                sys.exit()

    if vorgehen_1 == 3:
        sys.exit()

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

    abfrage_vorgehen()

    return

# ----------------------------------------------------------------------------------------------------------------------
