import pandas as pd
# from datetime import date
# import numpy as np
# import calendar

# today = date.today()
# date_today = today.strftime("%Y-%m-%d")
# print(date_today)

## aktuellen Datensatz des RKI importieren

# dataset_rki = pd.read_csv('https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland/blob/main/Aktuell_Deutschland_SarsCov2_Infektionen.csv')
# dataset_rki = []
dataset_rki = pd.read_csv('C:\\Users\\Kai\\Documents\\GitHub\\Projekt_Datascience\\Datensatz_Neuinfektionen_gesamt.csv', low_memory=False)

# dataset_rki = pd.read_csv(f'https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland_Archiv/blob/master/Archiv/{date_today}_Deutschland_SarsCov2_Infektionen.csv')



# dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
tab_lk = pd.read_csv('C:\\Users\\Kai\\Documents\\GitHub\\Projekt_Datascience\\Liste_der_Landkreise_fuer_Projekt.csv')

# groupby the desired column and iterate through the groupby object

#print(dataset_rki)
#print(type(dataset_rki))

#print(dataset_rki['IdLandkreis'])

for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    #print(Id_lk)
    #print(dataset_rki)
    row_lk = tab_lk.loc[tab_lk["IdLandkreis"] == Id_lk]
    #row_lk = tab_lk.loc[tab_lk["IdLandkreis"] == f'{IdLandkreis}']
    #row_lk = tab_lk.loc[tab_lk["IdLandkreis"] == dataset_rki[0]]
    #print(row_lk)
    #print(type(row_lk))
#    print(shape(row_lk))
    #number_lk = row_lk["IdLandkreis"].values[0]
    #print(number_lk)
    #name_lk = row_lk['NameLandkreis'].values[0]
    name_lk = row_lk['NameLandkreis']
    print(name_lk)
    ## save the dataframe for each group to a csv; seperated for each Landkreis
    #dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk}.csv', index=False, mode='a')
    #dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{number_lk}.csv', index=False, mode='a')
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{Id_lk}.csv', index=False, mode='a')
    # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\{number_lk}_{name_lk}.csv', index=False, mode='a')
