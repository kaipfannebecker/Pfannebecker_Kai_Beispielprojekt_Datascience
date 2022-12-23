import pandas as pd
import numpy as np
import shutil

# Importieren der Listen Landkreise_org

lk_org = pd.read_csv("liste_landkreise_org.csv", dtype=str, skiprows=[0], header=None)

# Löschen der Zellen mit leeren Einträgen

lk_org.replace('', np.nan, inplace=True)
lk_org.dropna(inplace=True)

# Ändern der Datentypen der Identifier in String
lk_org[0] = lk_org[0].apply(str)


# Importieren der Liste vom RKI

lk_rki = pd.read_csv("liste_rki.csv", header=None)

# Ändern der Datentypen der Identifier in String
lk_rki[0] = lk_rki[0].apply(str)


# Kombinieren der Dataframes

listen = [lk_org, lk_rki]
lk_fin = pd.concat(listen)



# Berlin_gesamt_löschen
berlin = lk_fin[0].str.contains('11000')

# Berlin_gesamt entfernen
## trennt Daten des RKI in verschiedene Unterbezirke auf

## Nach Code 11000 suchen und spalte mit True oder False hinzufügen
lk_fin['berlin'] = lk_fin[0].str.contains('11000')

## Alle Zeilen mit berlin = True löschen

lk_fin = lk_fin[lk_fin.berlin != True]

## Spalte berlin löschen

lk_fin = lk_fin.drop(columns=lk_fin.columns[2])


# sortieren nach Identifiern

lk_fin = lk_fin.sort_values([0])

# Identifier umwandeln in integer

lk_fin[0] = pd.to_numeric(lk_fin[0])

# Als .csv Datei ausgeben

lk_fin.to_csv("Liste_der_Landkreise_fuer_Projekt.csv", index=False)

# File in den Hauptordner kopieren
shutil.copy('Liste_der_Landkreise_fuer_Projekt.csv' , r'C:\Users\Kai\Desktop\Projekt_Datascience')  # dst can be a folder; use shutil.copy2() to preserve timestamp
