import pandas as pd

# Ließt Idenitifier und Namen der Landkreise ein; ACHTUNG: resultierender Datatype String!
##lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=[0, 1, 2, 3, 4, 5], na_values=['NA'],
                      #usecols=["C, D, E, F, H"], skiprows=[0, 1, 2, 4])
lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=6, usecols='C:F, H',
                      na_values=['NA'], dtype=str)

#lk_all.to_csv("liste_LK.csv")

#lk_all = lk_all.drop(index=[0], columns=[0])
#print(lk_all)

## kopiert alle Landkreise (d. h. alle Einträge mit NaN in VB) in neue Datei

lk_small = lk_all[lk_all['Unnamed: 5'].isna()]

# Alle Regionen (d.h. kombinierte Landkreise) entfernen
## haben nur eine einstellige Zahl in Spalte D

## Länge von Spalte D messen und in neue Spalte "length" anfügen
lk_small['length'] = lk_small["Unnamed: 4"].str.len()

# Alle Zeilen mit length = 1 löschen

lk_small = lk_small[lk_small.length != 1]

# Spalte length löschen

lk_small = lk_small.drop(columns=lk_small.columns[5])

## Zellen C, D, E zu einer Nummer verbinden

zweiter_wert = lk_small["Unnamed: 3"]
dritter_wert = lk_small["Unnamed: 4"]

lk_small["01"] = lk_small["01"].str.cat(zweiter_wert)
lk_small["01"] = lk_small["01"].str.cat(dritter_wert)

# löschen der Zeilen D und E sowie VB

lk_small = lk_small.drop(columns=lk_small.columns[3])
lk_small = lk_small.drop(columns=lk_small.columns[2])
lk_fin = lk_small.drop(columns=lk_small.columns[1])

## Identifier in String umwandeln
#lk_fin[0] = lk_fin[0].astype("string")
#print(lk_fin[0].apply(type))

# csv ausgeben

lk_fin.to_csv("liste_landkreise_org.csv", index=False)
