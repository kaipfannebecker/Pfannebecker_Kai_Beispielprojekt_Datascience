import pandas as pd
import numpy as np

# Importieren der Listen Landkreise_org

#lk_org = pd.read_csv("liste_landkreise_org.csv", dtype = str, skiprows=[0], header=None)
lk_org = pd.read_csv("liste_landkreise_org.csv", dtype = str, skiprows=[0], header=None)

# Importieren der Liste vom RKI

lk_rki = pd.read_csv("liste_rki.csv", header=None)

# Kombinieren der Dataframes

listen = [lk_org, lk_rki]
lk_fin = pd.concat(listen)

# Löschen der Zellen mit leeren Einträgen

lk_fin.replace('', np.nan, inplace=True)
lk_fin.dropna(inplace=True)



lk_fin.to_csv("Liste_der_Landkreise_fuer_Projekt.csv", index=False)

# print(Liste_Landkreise_final)
# print(lk_org)
# print(lk_rki)