import logging
import sys

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## fragt die gewünschte Ebene ab

# Benötigt:
## -

# Gibt zurück:
## Variable: "ebene"


# ----------------------------------------------------------------------------------------------------------------------


def abfrage_variablen_ebene():
    # Abfrage Ebene:
    try:
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

        pos_values = [1, 2, 3, 4, 5]

        if ebene not in pos_values:
            print("Ihre Eingabe konnte nicht zugeordnet werden.")
            logging.warning(f"Unbekannte Eingabe. Die Eingabe konnte nicht zugeordnet werden.")
            abfrage_variablen_ebene()

    except SyntaxError:
        print("Ihre Eingabe konnte nicht zugeordnet werden.")
        logging.warning(f"Syntax Error. Die Eingabe konnte nicht zugeordnet werden.")
        abfrage_variablen_ebene()

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
