import json
import pandas as pd
data_neuinf_ges = []
data_neuinf_ges = pd.DataFrame(data_neuinf_ges)
data = []
with open('data_2020-04-26-04-06.ndjson') as f:
    for line in f:
        data.append(json.loads(line))
#print(type(data))
df = pd.DataFrame(data)
#print(df.head())
df = df.drop(columns=["DatenstandISO","RefdatumISO","Refdatum","Datenstand","ObjectId","Meldedatum"])
nur_neu = df.loc[df["NeuerFall"] == 1]
nur_corr = df.loc[df["NeuerFall"] == -1]
neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
print(nur_neu.size)
print(nur_corr.size)

data_neuinf_ges_2 = pd.concat(neue_daten)
#nur_neu.append(data_neuinf_ges)
#nur_corr.append(data_neuinf_ges)
print(data_neuinf_ges_2.size)
data_neuinf_ges_2.to_csv("Datensatz_Neuinfektionen_gesamt.csv")

#'B', 'C'