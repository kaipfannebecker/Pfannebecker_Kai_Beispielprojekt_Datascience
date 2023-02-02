import logging
import sys

from Methoden.Auswertung.Helper import aktualitaet

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## fragt dsa gewünschte Vorgehen ab

# Benötigt:
## -

# Gibt zurück:
## Auswahl der Aktualität des Datensatzes


# ----------------------------------------------------------------------------------------------------------------------


def abfrage_vorgehen():
    try:
        vorgehen_1 = eval(input(
            "Möchten Sie die Data_collection zuerst aktualisieren oder die vorhandenen Data_collection "
            "direkt auswerten? \n"
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

                else:
                    print("Ihre Eingabe konnte nicht zugeordnet werden.")

        if vorgehen_1 == 3:
            sys.exit()

        pos_values = [1, 2, 3]

        if vorgehen_1 not in pos_values:
            print("Ihre Eingabe konnte nicht zugeordnet werden.")
            logging.warning(f"Unbekannte Eingabe. Die Eingabe konnte nicht zugeordnet werden.")
            abfrage_vorgehen()()

    except SyntaxError:
        print("Ihre Eingabe konnte nicht zugeordnet werden.")
        logging.warning(f"Syntax Error. Die Eingabe konnte nicht zugeordnet werden.")
        abfrage_vorgehen()()

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
