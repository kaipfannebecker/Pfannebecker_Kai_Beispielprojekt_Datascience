import pandas as pd
import matplotlib.pyplot as plt
import numpy

dataset_final = pd.read_csv{"1004.csv"}

# erstellt den ursprünglichen Datensatz
anzfae_lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

## iterieren über die einzelnen Daten von startdatum bis enddatum

for meld_dat, dataset_final in dataset_final.groupby('Meldedatum'):
    data_neu = dataset_final.loc[[6] == 1]
    data_neu.sum([6])
    fall_t = {f"{meld_dat}",data_neu.sum([9])}
    anzfae_lk_vs_t = anzfae_lk_vs_t.append(fall_t, ignore_index=True)


