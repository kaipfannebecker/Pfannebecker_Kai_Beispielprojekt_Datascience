import pandas as pd

# Ließt Idenitifier und Namen der Landkreise ein; ACHTUNG: resultierender Datatype String!
##lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=[0, 1, 2, 3, 4, 5], na_values=['NA'],
                      #usecols=["C, D, E, F, H"], skiprows=[0, 1, 2, 4])
lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=6, usecols='C:F, H',
                      na_values=['NA'], dtype=str)

#lk_all.to_csv("liste_LK.csv")
print(lk_all)

#lk_all = lk_all.drop(index=[0], columns=[0])
#print(lk_all)

## kopiert alle Landkreise (d. h. alle Einträge mit NaN in VB) in neue Datei

lk_small = lk_all[lk_all['Unnamed: 5'].isna()]

print(lk_small)

## Zellen C, D, E zu einer Nummer verbinden

zweiter_wert = lk_small["Unnamed: 3"]
print(zweiter_wert)
dritter_wert = lk_small["Unnamed: 4"]
print(dritter_wert)
print(lk_small["01"])
lk_small["01"] = lk_small["01"].str.cat(zweiter_wert)
lk_small["01"] = lk_small["01"].str.cat(dritter_wert)

# löschen der Zeilen D und E sowie VB

lk_small = lk_all.drop(columns=lk_small.columns[3])
lk_small = lk_all.drop(columns=lk_small.columns[2])
lk_small = lk_all.drop(columns=lk_small.columns[1])

print(lk_small)
#lk_fin = lk_small

## csv ausgeben
#lk_fin.to_csv("lk_fin.csv")

# als csv Datei ausgeben
# lk_fin.to_csv("landkreise.csv")

## Delete rows where case numbers are zero
## This deletion is completed by "selecting" rows where case numbers are non zero
# data = data.loc[data["cases"] != 0]
# data.shape

# lk_small = lk_big.loc(lk_big["VB"] != "NaN")