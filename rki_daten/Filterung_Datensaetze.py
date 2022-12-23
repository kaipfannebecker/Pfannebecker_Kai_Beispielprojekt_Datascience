import pandas as pd
import numpy as np

#dataset_rki = []
dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
tab_lk = pd.read_csv(r'C:\Users\Kai\Desktop\Projekt_Datascience\Liste_der_Landkreise_fuer_Projekt.csv')

# groupby the desired column and iterate through the groupby object

for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    row_lk = tab_lk.loc[tab_lk["0"] == Id_lk]
    number_lk = row_lk['0'].values[0]
    name_lk = row_lk['1'].values[0]
    # save the dataframe for each group to a csv
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk}.csv', index=False, mode='a')
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{number_lk}.csv', index=False, mode='a')
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\{number_lk}_{name_lk}.csv', index=False, mode ='a')