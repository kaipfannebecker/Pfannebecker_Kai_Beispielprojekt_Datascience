import logging
from Methoden.Datengeneration.Landkreise_Bundeslaender.Helper \
    import liste_landkreise, liste_rki, combine_Listen_Landkreise, bundeslaender


# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ordnet die einzelnen Landkreise_Bundeslaender den jeweiligen Bundesländern zu.

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------


def main():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
                                  'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Liste Landkreise generieren
    liste_landkreise.main()
    liste_rki.main()
    combine_Listen_Landkreise.main()

    # Liste Bundesländer generieren
    bundeslaender.main()

    logging.info("Die Listengeneration ist abgeschlossen.")
