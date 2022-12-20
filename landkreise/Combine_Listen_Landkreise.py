import pandas as pd

# Importieren der Listen Landkreise_org

lk_org = pd.read_csv("liste_landkreise_org.csv", dtype = str, skiprows=[0], header=None)

# Löschen der hinzugefügten Zeile
lk_org.drop(columns=lk_org.columns[0])

# Importieren der Liste vom RKI

# lk_rki = pd.read_csv("liste_rki.csv", header=None)

# Kombinieren der Dataframes

#listen = [lk_org_fin, lk_rki]
#Liste_Landkreise_final = pd.concat(listen)

#print(Liste_Landkreise_final)
print(lk_org_fin)
#print(lk_rki)