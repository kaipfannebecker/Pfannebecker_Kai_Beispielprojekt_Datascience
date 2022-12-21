import pandas as pd
import numpy as np

# Importieren der Listen Landkreise_org

lk_org = pd.read_csv("liste_landkreise_org.csv", dtype=str, skiprows=[0], header=None)

# Importieren der Liste vom RKI

lk_rki = pd.read_csv("liste_rki.csv", header=None)

# Kombinieren der Dataframes

listen = [lk_org, lk_rki]
lk_fin = pd.concat(listen)

# Löschen der Zellen mit leeren Einträgen

lk_fin.replace('', np.nan, inplace=True)
lk_fin.dropna(inplace=True)

# Berlin_gesamt_löschen
berlin = lk_fin[0].str.contains('11000')

# Berlin_gesamt entfernen
## trennt Daten des RKI in verschiedene Unterbezirke auf

## Nach Code 11000 suchen und spalte mit True oder False hinzufügen
lk_fin['berlin'] = lk_fin[0].str.contains('11000')

# Alle Zeilen mit berlin = True löschen

lk_fin = lk_fin[lk_fin.berlin != True]

# Spalte berlin löschen

lk_fin = lk_fin.drop(columns=lk_fin.columns[2])

# Als .csv Datei ausgeben

lk_fin.to_csv("Liste_der_Landkreise_fuer_Projekt.csv", index=False)
