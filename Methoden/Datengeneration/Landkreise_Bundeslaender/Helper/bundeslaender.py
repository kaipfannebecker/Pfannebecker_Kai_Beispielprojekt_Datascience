import logging
import pandas as pd
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ordnet die einzelnen Landkreise_Bundeslaender den jeweiligen Bundesländern zu.

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------


def create_liste_lk():
    # Datensatz Schleswig-Holstein hinzufügen
    sh_data = dict(A="01", B="Schleswig-Holstein")
    df = pd.DataFrame(sh_data, index=[0])
    bl_sh = df.rename(columns={"A": "01", "B": "Schleswig-Holstein"})

    # Liest Idenitifier und Namen der Bundesländer ein; ACHTUNG: resultierender Datatype String!
    bl_all = pd.read_excel(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\landkreise\AuszugGV2QAktuell.xlsx",
                           sheet_name=1, header=6, usecols='C:D, H', na_values=['NA'], dtype=str
                           )
    bl_small = bl_all[bl_all['Unnamed: 3'].isna()]
    bl_small_1 = bl_small.drop(columns=bl_small.columns[1])

    # Löschen der Zellen mit leeren Einträgen
    bl_small_1.replace('', np.nan, inplace=True)
    bl_small_1.dropna(inplace=True)

    # Kombiniert beide Datensätze
    bl_compl = pd.concat([bl_small_1, bl_sh], ignore_index=True)

    # Spalten umbenennen
    bl_compl = bl_compl.rename(columns={"01": "IdBundesland", "Schleswig-Holstein": "NameBundesland"})

    # Sortiert nach IdBundesland
    bl_compl = bl_compl.sort_values(by=['IdBundesland'])

    # Als .csv Datei ausgeben
    bl_compl.to_csv(
        r".\Liste_der_Bundeslaender_fuer_Projekt.csv", index=False
    )


def main():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    create_liste_lk()

# main()
