import pandas as pd
import os
import logging

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Sortiert alle Datensätze in "zu_sort" nach der Spalte "Meldedatum"

# Benötigt:
## Übergabe von String mit den gewünschten Datensätzen als "zu_sort"
## in der ersten Spalte nach dem Index als dataframe zu_akt

# Gibt zurück:
## sort = 1 als Nachweis, das Modul durchgelaufen ist

# ----------------------------------------------------------------------------------------------------------------------
# Logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)
# ----------------------------------------------------------------------------------------------------------------------
################################################# Definierte Funktionen ################################################
# ----------------------------------------------------------------------------------------------------------------------


def main(zu_sort, anz_sort):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    sort = sorting(zu_sort, anz_sort)
    logger.info(f'Datensatz nach MeldedatumISO sortiert, returncode: sort = {sort}')

    return sort


def sorting(zu_sort, anz_sort):
    directory = os.fsencode(
        r"/rki_daten/Datensatz_vereinzelt/by_number"
    )

    # Iteriere über alle Files in einem Ordner
    if anz_sort == 1:
        filename = f"{zu_sort}.csv"
        dataframe = pd.read_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{filename}")
        dataframe.sort_values(by=["MeldedatumISO"])
        logging.info(f'Der Datensatz {zu_sort} wurde nach MeldedatumISO sortiert.')
        dataframe.to_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{filename}.csv")
    else:
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            # suche nach .csv Dateien
            if filename.endswith(".csv"):
                dataframe = pd.read_csv(filename)
                dataframe.sort_values(by=["MeldedatumISO"])
                dataframe.to_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{filename}.csv")
    sort = 1
    return sort


# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------


# zu_sort = 1001
# anz_sort = 1
# main(zu_sort, anz_sort)
