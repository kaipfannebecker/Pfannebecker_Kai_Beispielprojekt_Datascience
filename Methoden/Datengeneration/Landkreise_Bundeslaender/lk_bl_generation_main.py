import logging

from Methoden.Datengeneration.Landkreise_Bundeslaender.Helper \
    import liste_landkreise, liste_rki, combine_Listen_Landkreise, bundeslaender


# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## erzeugt die Liste der Landkreise sowie die Liste der Bundesländer

# Benötigt:
## Module: liste_landkreise.py, liste_rki.py, combine_Listen_Landkreise.py, bundeslaender.py

# Gibt zurück:
## zwei separate Listen: einmal mit Bundesländern, einmal mit Landkreisen

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
    logging.info("Die Liste der Landkreise wurde generiert.")
    liste_rki.main()
    logging.info("Die Liste der Berliner Bezirke  wurde erstellt.")
    combine_Listen_Landkreise.main()
    logging.info("Beide Listen wurden vereinigt.")

    # Liste Bundesländer generieren
    bundeslaender.main()
    logging.info("Die Liste der Bundesländer ist generiert.")

    logging.info("Die Listengeneration ist abgeschlossen.")
