import pandas as pd
from datetime import date
# import numpy as np
# import calendar

# today = date.today()
# date_today = today.strftime("%Y-%m-%d")
# print(date_today)

## aktuellen Datensatz des RKI importieren

# dataset_rki = pd.read_csv('https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland/blob/main/Aktuell_Deutschland_SarsCov2_Infektionen.csv')
dataset_rki = pd.read_csv('https://media.githubusercontent.com/media/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland/main/Aktuell_Deutschland_SarsCov2_Infektionen.csv')

# dataset_rki = pd.read_csv(f'https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland_Archiv/blob/master/Archiv/{date_today}_Deutschland_SarsCov2_Infektionen.csv')


# dataset_rki = []
# dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
tab_lk = pd.read_csv(r'C:\Users\Kai\Desktop\Projekt_Datascience\Liste_der_Landkreise_fuer_Projekt.csv')

# groupby the desired column and iterate through the groupby object

for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    row_lk = tab_lk.loc[tab_lk["0"] == Id_lk]
    number_lk = row_lk['0'].values[0]
    # name_lk = row_lk['1'].values[0]
    ## save the dataframe for each group to a csv; seperated for each Landkreis
    # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk}.csv', index=False, mode='a')
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{number_lk}.csv', index=False, mode='a')
    # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\{number_lk}_{name_lk}.csv', index=False, mode='a')
