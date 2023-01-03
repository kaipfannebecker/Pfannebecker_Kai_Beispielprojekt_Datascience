import pandas as pd
import matplotlib.pyplot as plt
import numpy

# erstellt den ursprünglichen Datensatz
# lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

#dataset_final = pd.read_csv("test_datei.csv")
#print(type(dataset_final))
#print(dataset_final[:,9])
# iterieren über die einzelnen Daten von startdatum bis enddatum

#for meld_dat, dataset_final in dataset_final.groupby('Meldedatum'):
#data_neu = dataset_final.loc[dataset_final['NeuerFall'] == 1]
    # print(data_neu)
    # dataset_final.to_csv(f'{meld_dat}.csv', index=False, mode='a')
anz_fae = [10, 12, 14, 11, 13] #data_neu.sum()
    #print(anz_fae)
    #print(meld_dat)
    #dataset_final.sum(anz_fae) #["AnzahlFall"] #tuple([9])
meld_dat = ["2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06","2022-12-07"]
lk_vs_t = [["2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06","2022-12-07"],[10, 12, 14, 11, 13]]
# fall_t = {[meld_dat, anz_fae]} # funktioniert
#print(fall_t)
# print(type(lk_vs_t))
#lk_vs_t = lk_vs_t.append(fall_t, ignore_index=True)
# df.loc[df['favorite_color'] == 'yellow']
# print(lk_vs_t)

date = lk_vs_t[0]
faelle = lk_vs_t[1]

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([date], [faelle]);  # Plot some data on the axes.