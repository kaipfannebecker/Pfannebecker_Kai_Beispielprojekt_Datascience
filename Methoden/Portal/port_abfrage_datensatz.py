import logging
import sys

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## fragt den gewünschten Datensatz ab

# Benötigt:
## -

# Gibt zurück:
## Variable: "datensatz"

# ----------------------------------------------------------------------------------------------------------------------


def abfrage_variablen_datensatz():
    # Abgefragter Datensatz:
    try:
        datensatz = eval(input(
            "Welche Data_collection möchten Sie angezeigt haben:\n"
            "1) Neue Fälle\n"
            "2) Neue Genesene\n"
            "3) Neue Todesfälle\n"
            "4) zurück zur vorherigen Auswahl\n"
            "5) Abbruch\n"
            " "
        ))

        if datensatz == 5:
            sys.exit()

        if datensatz == 4:
            sys.exit()  # to change

        if datensatz == 5:
            sys.exit()

        pos_values = [1, 2, 3, 4, 5]

        if datensatz not in pos_values:
            print("Ihre Eingabe konnte nicht zugeordnet werden.")
            logging.warning(f"Unbekannte Eingabe. Die Eingabe konnte nicht zugeordnet werden.")
            abfrage_variablen_datensatz()

    except SyntaxError:
        print("Ihre Eingabe konnte nicht zugeordnet werden.")
        logging.warning(f"Syntax Error. Die Eingabe konnte nicht zugeordnet werden.")
        abfrage_variablen_datensatz()

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
