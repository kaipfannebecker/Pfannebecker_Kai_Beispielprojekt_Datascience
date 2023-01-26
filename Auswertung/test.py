import pandas as pd
import matplotlib.pyplot as plt
import numpy

dataset_final = pd.read_csv("1004.csv")
#print(type(dataset_final))
#print(dataset_final)

# erstellt den ursprünglichen Datensatz
anzfae_lk_vs_t = pd.DataFrame(columns=["Datum", "Gesamtzahl neue Infektionen"])
#print(anzfae_lk_vs_t)
#print(type(anzfae_lk_vs_t))

## iterieren über die einzelnen Data_collection von startdatum bis enddatum

# meld_dat,

for datum, dataset_final_1 in dataset_final.groupby('Meldedatum'):
    # data_neu = dataset_final.loc[[6] == "1"]
    # df = df.loc[df['y'] == D]
    data_zwischen = dataset_final_1.loc[dataset_final_1["Meldedatum"] == datum]
    # bis hierhin funktioniert es
    #data_zwischen.to_csv(f"data_zwischen{datum}.csv")
    data_neu = data_zwischen["NeuerFall"] == "1"
    print(data_neu)
#    data_neu = data_zwischen.loc[data_zwischen["NeuerFall"] == 1]
    #data_neu = data_zwischen.loc[data_zwischen["NeuerFall"] == "1"]
    #data_neu.to_csv(f"data_neu{datum}.csv")
    #faelle = data_neu["AnzahlFall"].sum()
    # ab hier funktioniert
    #fall_t = [[datum], [faelle]]
    #anzfae_lk_vs_t.loc[len(anzfae_lk_vs_t)] = fall_t
    #print(anzfae_lk_vs_t)

