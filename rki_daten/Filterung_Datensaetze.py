import pandas as pd
import numpy as np

#dataset_rki = []
dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
tab_lk = pd.read_csv(r'C:\Users\Kai\Desktop\Projekt_Datascience\Liste_der_Landkreise_fuer_Projekt.csv')

#print(landkreise)
#print(dataset_rki)

# groupby the desired column and iterate through the groupby object
#for group, dataframe in df.groupby('Gene'):
#    # save the dataframe for each group to a csv
#    dataframe.to_csv(f'{group}.csv', index=False)
#print(landkreise["0"])
#Path = '.\Projekt_Datascience'

for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    row_lk = tab_lk.loc[tab_lk["0"] == Id_lk]
    #name_lk = row_lk["1"]
    name_lk = row_lk['1'].values[0]
    #val = d2['col_name'].values[0]
    #print(name_lk)
    #print(type(name_lk))
    # save the dataframe for each group to a csv
    #dataset_rki.to_csv('name_lk.csv', index=False)
    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\{name_lk}.csv', index=False)



#    Path = './Result/Normal'
 #   for i in range(1, 151):
 #       Normal_i.to_csv(Path + str(i), sep=',', header=None, index=None)