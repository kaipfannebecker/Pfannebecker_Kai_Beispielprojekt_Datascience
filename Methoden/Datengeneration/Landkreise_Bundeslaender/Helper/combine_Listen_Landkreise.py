import numpy as np
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ruft "liste_landkreise_org.csv" auf, kombiniert diese mit der in "liste_rki.csv" gespeicherten Aufteilung für Berlin,
## löscht den kombinierten Landkreis Berlin und gibt dann die resultierende Liste
## als "Liste_der_Landkreise_fuer_Projekt.csv" aus.

# Benötigt:
## liste_landkreise_org.csv
## liste_rki.csv

# Gibt zurück:
## Datei "Liste_der_Landkreise_fuer_Projekt.csv"

# ----------------------------------------------------------------------------------------------------------------------

## zu Testzwecken:


# ----------------------------------------------------------------------------------------------------------------------

def combine_lk_lists():

    # Importieren der Listen Landkreise_org
    lk_org = pd.read_csv("./landkreise/liste_landkreise_org.csv", dtype=str, skiprows=[0], header=None)

    # Löschen der Zellen mit leeren Einträgen
    lk_org.replace('', np.nan, inplace=True)
    lk_org.dropna(inplace=True)

    # Ändern der Datentypen der Identifier in String
    lk_org[0] = lk_org[0].apply(str)

    # Importieren der Liste vom RKI
    lk_rki = pd.read_csv("./landkreise/liste_rki.csv", header=None)

    # Ändern der Datentypen der Identifier in String
    lk_rki[0] = lk_rki[0].apply(str)

    # Kombinieren der Dataframes
    listen = [lk_org, lk_rki]
    lk_fin = pd.concat(listen)

    # Berlin_gesamt_löschen
    berlin = lk_fin[0].str.contains('11000')

    # Landkreis Berlin_gesamt entfernen
    ## trennt Data_collection des RKI in verschiedene Unterbezirke auf
    ## nach Code 11000 suchen und spalte mit True oder False hinzufügen
    lk_fin['berlin'] = lk_fin[0].str.contains('11000')
    ## Alle Zeilen mit berlin = True löschen
    lk_fin = lk_fin[lk_fin.berlin != True]

    ## Spalte berlin löschen
    lk_fin = lk_fin.drop(columns=lk_fin.columns[2])

    # Spalten umbenennen
    lk_fin.rename(columns={"0": "LandkreisIdentifier", "1": "LandkreisName"})

    # sortieren nach Identifiern
    lk_fin = lk_fin.sort_values([0])

    # Identifier umwandeln in integer
    lk_fin[0] = pd.to_numeric(lk_fin[0])

    # Anführungszeichen in Namen der Landkreise_Bundeslaender entfernen
    lk_fin[1] = lk_fin[1].replace(",", ";")

    # Die Spalten in Id_Landkreis sowie Name_Landkreis umbenennen
    lk_fin.rename(columns={0: "IdLandkreis", 1: "NameLandkreis"}, inplace=True)

    # Als .csv Datei ausgeben
    lk_fin.to_csv(r".\Liste_der_Landkreise_fuer_Projekt.csv", index=False)


def main():
    combine_lk_lists()
