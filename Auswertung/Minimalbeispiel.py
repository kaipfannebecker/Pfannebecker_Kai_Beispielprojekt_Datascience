
import pandas as pd

import os

# ----------------------------------------------------------------------------------------------------------------------



empty_df = {"Gesamtzahl neue Infektionen": [0], "IdLandkreis": [0]}
anzfae_all_lk = pd.DataFrame(data=empty_df)

# Daten vom gewünschten Tag aus allen Landkreisen abfragen:
for file in os.listdir(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number"):
    if file.endswith(".csv"):
        data_single_lk = pd.read_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{file}")
        data_single_lk_neu = data_single_lk.loc[data_single_lk['MeldedatumISO'] == date]
        if data_single_lk_neu.empty:
            data_neu_ges = 0
        else:
            data_neu_pos_1 = data_single_lk_neu.loc[data_single_lk_neu['NeuerFall'] == 1.0]
            data_neu_pos = data_neu_pos_1.sum()
            data_neu_pos_num = data_neu_pos["AnzahlFall"]
            data_neu_neg_1 = data_single_lk_neu.loc[data_single_lk_neu["NeuerFall"] == -1.0]
            if data_neu_neg_1.empty:
                data_neu_neg_num = 0
            else:
                data_neu_neg = data_neu_neg_1.sum()
                data_neu_neg_num = data_neu_neg["AnzahlFall"]
            data_neu_ges = data_neu_pos_num + data_neu_neg_num
        number_lk = file.removesuffix('.csv')
        fall_t = {f"{number_lk}", data_neu_ges}
        fall_t = list(fall_t)
        #print(fall_t)
        # print(type(fall_t))
        anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = fall_t