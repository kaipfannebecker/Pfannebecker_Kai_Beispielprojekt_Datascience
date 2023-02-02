import logging

from Methoden.Datengeneration.Data_processing.Helper import filterung_dataset

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## ruft Module zur Datenprozessierung auf

# Benötigt:
## "filterung_dataset.py"

# Gibt zurück:
## -

# ----------------------------------------------------------------------------------------------------------------------



def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    filterung_dataset.main()
    logging.info("Data processing ist abgeschlossen")
