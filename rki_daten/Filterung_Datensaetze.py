import pandas as pd
import numpy as np

#dataset_rki = []
dataset_rki = pd.read_csv('2021-04-02_Deutschland_SarsCov2_Infektionen.csv')

#print(dataset_rki)

# groupby the desired column and iterate through the groupby object
#for group, dataframe in df.groupby('Gene'):
#    # save the dataframe for each group to a csv
#    dataframe.to_csv(f'{group}.csv', index=False)

for IdLandkreis, dataset_rki in dataset_rki.groupby('IdLandkreis'):
    # save the dataframe for each group to a csv
    dataset_rki.to_csv(f'{IdLandkreis}.csv', index=False)