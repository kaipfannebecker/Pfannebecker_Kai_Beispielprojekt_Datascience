import pandas as pd

# Ließt Idenitifier und Namen der Landkreise ein
lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=[0, 1, 2, 3, 4, 5], na_values=['NA'],
                      usecols=["C, D, E, F, H"])

# kopiert alle Landkreise (d. h. alle Einträge mit NaN in VB) in neue Datei
#lk_big = lk_all[lk_all['VB'].null()]
lk_big = lk_all.drop([nonull:=True], implace=False)

# löscht alle Zeilen, in denen die Spalte VB ausgefüllt ist
lk_small = lk_big.loc(lk_big["VB"])

# Zellen C, D, E zu einer Nummer verbinden

lk_fin = lk_small

# csv ausgeben
lk_fin.to_csv("lk_fin.csv")

# Hinzufügen von RKI spezifischen Landkreisen
## 11001 Berlin Mitte
## 11002 Berlin Friedrichshain-Kreuzberg
## 11003 Berlin Pankow
## 11004 Berlin Charlottenburg-Wilmersdorf
## 11005 Berlin Spandau
## 11006 Berlin Steglitz-Zehlendorf
## 11007 Berlin Tempelhof-Schöneberg
## 11008 Berlin Neukölln
## 11009 Berlin Treptow-Köpenick
## 11010 Berlin Marzahn-Hellersdorf
## 11011 Berlin Lichtenberg
## 11012 Berlin Reinickendorf

df_RKI = data.frame[(11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012,),
        ("Berlin Mitte", "Berlin Friedrichshain-Kreuzberg", "Berlin Pankow", "Berlin Charlottenburg-Wilmersdorf",
         "Berlin Spandau", "Berlin Steglitz-Zehlendorf", "Berlin Tempelhof-Schöneberg", "Berlin Neukölln",
         "Berlin Treptow-Köpenick", "Berlin Marzahn-Hellersdorf", "Berlin Lichtenberg", "Berlin Reinickendorf")]

df_RKI.to_csv("lk_fin.csv", mode='a')

# als csv Datei ausgeben
lk_fin.to_csv("landkreise.csv")

## Delete rows where case numbers are zero
## This deletion is completed by "selecting" rows where case numbers are non zero
# data = data.loc[data["cases"] != 0]
# data.shape

# lk_small = lk_big.loc(lk_big["VB"] != "NaN")