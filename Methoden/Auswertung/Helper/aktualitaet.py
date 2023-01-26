from datetime import datetime, timedelta, date
import sys
import logging
from Methoden.Datengeneration.Data_collection import data_collcetion_main
from Methoden.Datengeneration.Landkreise_Bundeslaender import lk_bl_generation_main
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ruft "anz_lk" Landkreise_Bundeslaender ab, prüft diese über das Submodul aktualitaet.py auf Aktualität
## und gibt die Liste der Landkreise_Bundeslaender "liste_lk" zurück

# Benötigt:
## Übergabe von String mit den gewünschten Datensätzen als "zu_akt"
## in der ersten Spalte nach dem Index als dataframe zu_akt

# Gibt zurück:
## akt = 1 als Nachweis, das Modul durchgelaufen ist

# ----------------------------------------------------------------------------------------------------------------------

## zu Testzwecken:
# akt = 1
# sort = 1
# anz_lk=2

# ----------------------------------------------------------------------------------------------------------------------


today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')
akt = 0
sort = 0
# NÖTIG: Übergabe von String mit den gewünschten Datensätzen
# in der ersten Spalte nach dem Index als dataframe zu_akt

# sort_meld.py aufrufen und Data_collection nach Meldedatum sortieren
# if sort <= 1:
    # zu_sort = zu_akt
    # runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")


def aktualisierung():
    vorgehen_akt = eval(input(
        "Wie genau möchten Sie die Data_collection aktualisieren?\n"
        "1) den aktuellen Datenstand anzeigen\n"
        "2) die Tabelle der Landkreise und Bundesländer (neu) anlegen\n"
        "3) Neue Data_collection herunterladen\n"
        "4) Data_collection (erneut) einlesen\n"
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
        data_collcetion_main.main(vorgehen_akt)

    if vorgehen_akt == 4:
        data_collcetion_main.main(vorgehen_akt)

    if vorgehen_akt == 5:
        print("zu implementieren")

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
