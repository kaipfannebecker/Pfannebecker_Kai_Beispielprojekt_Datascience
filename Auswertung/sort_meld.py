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
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------

def main():
    sort = sorting()
    return sort

def sorting():
    directory = os.fsencode("C:\Users\Kai\Desktop\Projekt_Datascience\Auswertung")

    # Iteriere über alle Files in einem Ordner
    if zu_sort == True and len(zu_sort) == 1:
        for file in os.listdir(directory):
        filename = zu_sort.csv
        dataframe = pd.read_csv(filename)
        dataframe.sort_values(by=[3])
        dataframe.to_csv(f"{filename}.csv")
    else:
        for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # suche nach .csv Dateien
            if filename.endswith(".csv"):
                dataframe = pd.read_csv(filename)
                dataframe.sort_values(by=[3])
                dataframe.to_csv(f"{filename}.csv")
    sort = 1
    return sort
