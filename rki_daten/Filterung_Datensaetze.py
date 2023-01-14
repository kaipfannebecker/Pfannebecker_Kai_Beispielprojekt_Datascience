import pandas as pd
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
## aktuellen Datensatz des RKI importieren

dataset_rki = pd.read_csv('C:\\Users\\Kai\\Documents\\GitHub\\Projekt_Datascience\\Datensatz_Neuinfektionen_gesamt.csv', low_memory=False)

# dataset_rki = pd.read_csv(f'https://github.com/robert-koch-institut/SARS-CoV-2-Infektionen_in_Deutschland_Archiv/blob/master/Archiv/{date_today}_Deutschland_SarsCov2_Infektionen.csv')


# dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
tab_lk = pd.read_csv('C:\\Users\\Kai\\Documents\\GitHub\\Projekt_Datascience\\Liste_der_Landkreise_fuer_Projekt.csv')

# groupby the desired column and iterate through the groupby object


for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    row_lk = tab_lk.loc[tab_lk["IdLandkreis"] == Id_lk]
    #if Id_lk != -1:
    #    name_lk = row_lk['NameLandkreis']
     #   #print(name_lk)
      #  #print(type(name_lk))
       # name_lk_2 = name_lk.iat[0]
        #print(name_lk_2)
        #dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk_2}.csv', index=False, mode='w')
    ## save the dataframe for each group to a csv; seperated for each Landkreis
    #dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{number_lk}.csv', index=False, mode='a')
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{Id_lk}.csv', index=False, mode='w')
    # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\{number_lk}_{name_lk}.csv', index=False, mode='a')
