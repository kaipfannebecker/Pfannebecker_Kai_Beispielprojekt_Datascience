import pandas as pd

# erstellt den ursprünglichen Datensatz
lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

dataset_final = pd.read_csv("1051.csv")

# iterieren über die einzelnen Daten von startdatum bis enddatum

for meld_dat, dataset_final in dataset_final.groupby('Meldedatum'):
    data_neu = dataset_final.loc[dataset_final["NeuerFall"] == 1]
    # print(data_neu)
    #dataset_final.to_csv(f'{meld_dat}.csv', index=False, mode='a')
    anz_fae = tuple([9])
    print(anz_fae)
    dataset_final.sum(anz_fae) #["AnzahlFall"] #tuple([9])
    fall_t = {meld_dat, data_neu.sum([9])}
    lk_vs_t = lk_vs_t.append(fall_t, ignore_index=True)
# df.loc[df['favorite_color'] == 'yellow']
#print(lk_vs_t)
