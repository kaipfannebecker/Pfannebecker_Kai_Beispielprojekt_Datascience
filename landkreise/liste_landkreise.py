import pandas as pd

# Ließt Idenitifier und Namen der Landkreise ein
##lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=[0, 1, 2, 3, 4, 5], na_values=['NA'],
                      #usecols=["C, D, E, F, H"], skiprows=[0, 1, 2, 4])
lk_all = pd.read_excel("AuszugGV2QAktuell.xlsx", sheet_name=1, header=6, usecols='C:F, H',
                      na_values=['NA'], dtype=str)

#lk_all.to_csv("liste_LK.csv")
print(lk_all)

#df = pd.read_excel("test.xlsx",
#                   sheet_name="test",
#                   header=2,
#                   index_col=[0,1],
#                   usecols='A:B,D:G',
#                   parse_dates=False)
#index = pd.read_excel("test.xlsx",
#                      sheet_name="test",
#                      header=None,
#                      skiprows=1,
#                      index_col=[0,1],
#                      nrows=2,
#                      usecols='A:B,D:G',
#                      parse_dates=False)
#index = index.fillna(method='ffill', axis=1)
#df.columns = pd.MultiIndex.from_arrays(index.values)
#df







# kopiert alle Landkreise (d. h. alle Einträge mit NaN in VB) in neue Datei
#lk_big = lk_all[lk_all['VB'].null()]
lk_big = lk_all.drop([nonull:=True], implace=False)

# löscht alle Zeilen, in denen die Spalte VB ausgefüllt ist
lk_small = lk_big.loc(lk_big["VB"])

# Zellen C, D, E zu einer Nummer verbinden

lk_fin = lk_small

# csv ausgeben
lk_fin.to_csv("lk_fin.csv")

# als csv Datei ausgeben
# lk_fin.to_csv("landkreise.csv")

## Delete rows where case numbers are zero
## This deletion is completed by "selecting" rows where case numbers are non zero
# data = data.loc[data["cases"] != 0]
# data.shape

# lk_small = lk_big.loc(lk_big["VB"] != "NaN")