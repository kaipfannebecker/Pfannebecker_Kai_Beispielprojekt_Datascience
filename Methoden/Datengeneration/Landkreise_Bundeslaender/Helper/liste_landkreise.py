import pandas as pd
import logging
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ordnet die einzelnen Landkreise_Bundeslaender den jeweiligen Bundesländern zu.

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------
def create_liste_lk():
    # Liest Idenitifier und Namen der Landkreise_Bundeslaender ein; ACHTUNG: resultierender Datatype String!
    lk_all = pd.read_excel(r"./landkreise/AuszugGV2QAktuell.xlsx",
                           sheet_name=1, header=6, usecols='C:F, H', na_values=['NA'], dtype=str
                           )

    ## kopiert alle Landkreise_Bundeslaender (d. h. alle Einträge mit NaN in VB) in neue Datei
    lk_small = lk_all[lk_all['Unnamed: 5'].isna()]

    # Spalte "IdBundesland" hinzufügen
    lk_small["IdBundesland"] = lk_small.loc[:, "01"]

    # Alle Regionen (d.h. kombinierte Landkreise_Bundeslaender) entfernen
    ## haben nur eine einstellige Zahl in Spalte D
    ## Länge von Spalte D messen und in neue Spalte "length" anfügen
    lk_small['length'] = lk_small["Unnamed: 4"].str.len()
    # Alle Zeilen mit length = 1 löschen
    lk_small = lk_small[lk_small.length != 1]
    # Spalte length löschen
    lk_small = lk_small.drop(columns=lk_small.columns[6])

    # -----------------------------------------------------------------------
    # Datensätze Landkreise nach Bundesländern geordnet erzeugen:
    dataset_double = lk_small

    bl_data = {
        "IdBundesland": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "NameBundesland": [
            "Schleswig-Holstein", "Hamburg", "Niedersachsen", "Bremen", "Nordrhein-Westfalen", "Hessen",
            "Rheinland-Pfalz", "Baden-Württemberg", "Bayern", "Saarland", "Berlin", "Brandenburg",
            "Mecklenburg-Vorpommern", "Sachsen", "Sachsen-Anhalt", "Thüringen"]
    }
    bl = pd.DataFrame(data=bl_data)

    for Id_bl, dataset_double in dataset_double.groupby('01'):
        Id_bl = int(Id_bl)-1
        name_bl = bl.iloc[Id_bl]["NameBundesland"]

        dataset_double['01'] = dataset_double['01'] + dataset_double["Unnamed: 3"] + dataset_double["Unnamed: 4"]

        # löschen der Zeilen D und E sowie VB
        dataset_double = dataset_double.drop(columns=dataset_double.columns[1])
        dataset_double = dataset_double.drop(columns=dataset_double.columns[1])
        dataset_double = dataset_double.drop(columns=dataset_double.columns[1])

        dataset_double = dataset_double.rename(columns={"01": "IdLandkreis"})

        nr = Id_bl+1

        ## save the dataframe for each group to a csv; seperated for each Bundesland
        dataset_double.to_csv(
            f'.\\landkreise\\nach_Bundesland\\Liste_Landkreise_in_{nr}_{name_bl}.csv', index=False, mode='w'
        )
    # -----------------------------------------------------------------------

    # Zellen C, D, E zu einer Nummer verbinden
    zweiter_wert = lk_small["Unnamed: 3"]
    dritter_wert = lk_small["Unnamed: 4"]

    lk_small["01"] = lk_small["01"].str.cat(zweiter_wert)
    lk_small["01"] = lk_small["01"].str.cat(dritter_wert)

    # löschen der Zeilen D und E sowie VB
    lk_small = lk_small.drop(columns=lk_small.columns[1])
    lk_small = lk_small.drop(columns=lk_small.columns[1])
    lk_fin = lk_small.drop(columns=lk_small.columns[1])

    # csv ausgeben
    lk_fin.to_csv("./landkreise/liste_landkreise_org.csv", index=False)


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
               'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    create_liste_lk()
