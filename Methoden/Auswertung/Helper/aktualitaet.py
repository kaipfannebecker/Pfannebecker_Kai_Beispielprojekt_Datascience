from datetime import datetime, timedelta, date

import logging
import sys

from Methoden.Datengeneration.Data_collection import data_collection_main
from Methoden.Datengeneration.Landkreise_Bundeslaender import lk_bl_generation_main
from Methoden.Datengeneration.Data_processing import data_processing_main
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## ruft die Submodule zur Aktualisierung des Datensatzes auf

# Benötigt:
## Module: data_collection_main.py,  lk_bl_generation_main.py, data_processing_main.py

# Gibt zurück:
## -

# ----------------------------------------------------------------------------------------------------------------------


today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')
akt = 0
sort = 0
# NÖTIG: Übergabe von String mit den gewünschten Datensätzen
# in der ersten Spalte nach dem Index als dataframe zu_akt


def aktualisierung():
    vorgehen_akt = eval(input(
        "Wie genau möchten Sie die Data_collection aktualisieren?\n"
        "1) den aktuellen Datenstand anzeigen\n"
        "2) die Tabelle der Landkreise und Bundesländer (neu) anlegen\n"
        "3) Neue Data_collection herunterladen\n"  # auf neue URLs prüfen
        "4) Data_collection (erneut) einlesen\n"  # URLs erneut herunterladen
        "5) 'Datensatz_Neuinfektionen_gesamt' (erneut) splitten\n" 
        "6) Zurück zur Auswertung\n"
        "7) Abbruch\n"
        "")
    )

    if vorgehen_akt == 1:
        print("zu implementieren")

    if vorgehen_akt == 2:
        lk_bl_generation_main.main()

    if vorgehen_akt == 3:
        data_collection_main.main(vorgehen_akt)

    if vorgehen_akt == 4:
        data_collection_main.main(vorgehen_akt)

    if vorgehen_akt == 5:
        data_processing_main.main()

    if vorgehen_akt == 6:
        print("zu implementieren")

    if vorgehen_akt == 7:
        sys.exit()


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    aktualisierung()
    # aktualisierung()
