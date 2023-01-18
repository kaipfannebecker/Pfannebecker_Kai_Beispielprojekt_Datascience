import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
import subprocess
import runpy
import os
from datetime import datetime, timedelta, date
today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Daten über das Module "aktualitaet.py" auf
## Aktualität und sortiert über "sort_meld.py" nach Meldedatum. Danach wird das Startdatum sowie Enddatum bestimmt und
## die Zahl der resultierenden Fälle pro Tag als Graph ausgegeben.

# Benötigt:
## "aufruf_lk.py"
## "aktualitaet.py"
## "sort_meld.py"

# Gibt zurück:
## 2d-Graph mit der x = Datum und Y = Anzahl Fälle

# ----------------------------------------------------------------------------------------------------------------------

## zu Testzwecken:
date = "2020-03-19"

# ----------------------------------------------------------------------------------------------------------------------

# Variablen:
# anz_lk = 1
# sort = 0
# akt = 0
# ----------------------------------------------------------------------------------------------------------------------

# Gesuchtes Datuma abfragen
# runpy.run_module(mod_name="datum", run_name= anz_lk) # , mod_name=f"{zu_akt}"
# return: date == YYYY-MM-DD

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
            data_neu_pos = data_single_lk_neu.loc[data_single_lk_neu['NeuerFall'] == 1.0]
            data_neu_pos = data_neu_pos.sum()
            data_neu_pos_num = data_neu_pos["AnzahlFall"]
            data_neu_neg = data_single_lk_neu.loc[data_single_lk_neu["NeuerFall"] == -1.0]
            if data_neu_neg.empty:
                data_neu_neg_num = 0
            else:
                data_neu_neg = data_neu_neg.sum()
                data_neu_neg_num = data_neu_neg["AnzahlFall"]
            data_neu_ges = data_neu_pos_num + data_neu_neg_num
        number_lk = file.removesuffix('.csv')
        fall_t = {f"{number_lk}", data_neu_ges}
        fall_t = list(fall_t)
        print(fall_t)
        # print(type(fall_t))
        anzfae_all_lk.loc[len(anzfae_all_lk)] = fall_t

print(type(anzfae_all_lk[1:1]))
print(anzfae_all_lk)
# TESTEN; TESTEN; TESTEN!