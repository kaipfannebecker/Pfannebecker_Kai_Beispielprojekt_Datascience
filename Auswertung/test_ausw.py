import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
import sys
import subprocess
import runpy
import os
import logging
import datumseingabe
import aktualitaet

# import datumseingabe
# from datetime import datetime, timedelta, date
#today = date.today()
#yesterday = datetime.now() - timedelta(1)
#datetime.strftime(yesterday, '%Y-%m-%d')
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
# date = "2020-08-20"

# ----------------------------------------------------------------------------------------------------------------------

# Variablen:
# anz_lk = 1
# sort = 0
# akt = 0
data_neu_ges = 0
global anz_date
anz_date = 1
laufvar_laender = 1

# ----------------------------------------------------------------------------------------------------------------------
# Logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)

# ----------------------------------------------------------------------------------------------------------------------
# Definierte Funktionen:
def data_test(): # muss noch getestet werden
    with open(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\urls_used.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        global date_dataset
        date_dataset = last_line[82:92]

def data_recovery(var_da_sort, var_da_anz):
    data_neu_pos_1 = data_single_lk_neu.loc[data_single_lk_neu[f'{var_da_sort}'] == 1.0]
    data_neu_pos = data_neu_pos_1.sum()
    data_neu_pos_num = data_neu_pos[f"{var_da_anz}"]
    data_neu_neg_1 = data_single_lk_neu.loc[data_single_lk_neu[f"{var_da_sort}"] == -1.0]
    if data_neu_neg_1.empty:
        data_neu_neg_num = 0
    else:
        data_neu_neg = data_neu_neg_1.sum()
        data_neu_neg_num = data_neu_neg[f"{var_da_anz}"]
    global data_neu_ges
    data_neu_ges = data_neu_pos_num + data_neu_neg_num

def data_lk(anzfae_all_lk_1):
    anzfae_all_lk_1['IdLandkreis'] = anzfae_all_lk_1['IdLandkreis'].astype(str)
    for index in anzfae_all_lk_1:
        anzfae_all_lk_1['IdLandkreis'] = anzfae_all_lk_1['IdLandkreis'].str.zfill(5)

def data_laender(var_da, anzfae_all_lk_1, laufvar_laender):
    dataset_empt = {var_da: [0], "IdBundesland": [0]}
    # Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
    dataset = pd.DataFrame(data=dataset_empt)
    if laufvar_laender < 17:
        print(laufvar_laender)
        print(anzfae_all_lk_1)
        anzfae_all_lk_neu_1 = anzfae_all_lk_1.loc[anzfae_all_lk_1['IdBundesland'] == laufvar_laender]
        anzfae_all_lk_neu = anzfae_all_lk_neu_1.sum()
        print(anzfae_all_lk_neu)
        #anzfae_all_lk_neu_ges = anzfae_all_lk_neu[f"{var_da_anz}"]
        #anzfae_all_lk_neu_ges = anzfae_all_lk_neu[f"{var_da}"]
        #dataset = {f"{number_lk}", anzfae_all_lk_neu_ges, IdBundesland}
        dataset = {f"{number_lk}", anzfae_all_lk_neu, IdBundesland}
        dataset = list(dataset)
        anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = dataset
        laufvar_laender = laufvar_laender + 1

def data_bund(var_da, anzfae_all_lk_1):
    dataset_empt = {var_da: [0], "Bundesgebiet": "Bundesgebiet"}
    # Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
    dataset = pd.DataFrame(data=dataset_empt)
    anzfae_all_lk_neu = anzfae_all_lk_1.sum()
    anzfae_all_lk_neu_ges = anzfae_all_lk_neu[f"{var_da_anz}"]
    dataset = {anzfae_all_lk_neu_ges, "Bundesgebiet"}
    dataset = list(dataset)
    anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = dataset

# ----------------------------------------------------------------------------------------------------------------------
# Abfrage Ebene:
ebene = eval(input("Auf welcher Ebene möchten Sie die Daten betrachten:\n"
                   "1) Landkreise\n"
                   "2) Bundesländer\n"
                   "3) Bundesgebiet\n"
                   "4) Abbruch\n"
                   " "))

if ebene == 4:
    sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
# Abgefragter Datensatz:
datensatz = eval(input("Welche Daten möchten Sie angezeigt haben:\n"
                       "1) Neue Fälle\n"
                       "2) Neue Genesene\n"
                       "3) Neue Todesfälle\n"
                       "4) Abbruch\n"
                       " "))
if ebene == 4:
    sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
# Gesuchtes Datum abfragen

datumseingabe.eindatum()
date = datumseingabe.datum
print("---------------------------------------------------------")
print(date)
print("---------------------------------------------------------")

# ----------------------------------------------------------------------------------------------------------------------
# Prüfen ob gewünschtes Datum im Datensatz vorhanden ist:
#print("test1")
data_test()
# funktioniert

if date_dataset > date or date_dataset == date:
    print("Das gewünschte Datum ist im Datensatz vorhanden.")
if date_dataset < date:
    entscheidung = eval(input("Das gewünschte Datum ist nicht im Datensatz vorhanden. Sie können nun entweder:"
          "1) Ein neues Datum eingeben"
          "2) Den Datensatz aktualisieren"
          "3) Den Vorgang abbrechen "))
    if entscheidung == 1:
        datumseingabe.eindatum()
        date = datumseingabe.datum
    if entscheidung == 2:
        #aktualitaet.eindatum()
        #date = datumseingabe.datum
        data_test()
    if entscheidung == 3:
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------
# Generieren des leeren Dataframes sowie der Parameter passend zur Eingabe:
if ebene == 1:
    var_eb = "IdLandkreis"
if ebene == 2:
    var_eb = "IdBundesländer"
if ebene == 3:
    var_eb = "IdBund"

if datensatz == 1:
    var_da = "Gesamtzahl neue Infektionen"
    var_da_sort = 'NeuerFall'
    var_da_anz = "AnzahlFall"
    var_da_verb = "infected"

if datensatz == 2:
    var_da = "Gesamtzahl neue Genesene"
    var_da_sort = 'NeuGenesen'
    var_da_anz = "AnzahlGenesen"
    var_da_verb = "recovered"

if datensatz == 3:
    var_da = "Gesamtzahl neue Todesfälle"
    var_da_sort = 'NeuerTodesfall'
    var_da_anz = "AnzahlTodesfall"
    var_da_verb = "killed"


empty_df = {var_da: [0], "IdLandkreis": [0], "IdBundesland": [0]}
# Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
anzfae_all_lk_1 = pd.DataFrame(data=empty_df)
#print(anzfae_all_lk_1)
#print(type(anzfae_all_lk_1))

# ----------------------------------------------------------------------------------------------------------------------
# Daten vom gewünschten Tag aus allen Landkreisen abfragen:
for file in os.listdir(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number"):
    if file.endswith(".csv"):
        data_single_lk = pd.read_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{file}")
        IdBundesland = data_single_lk.iloc[0]['IdBundesland']
        #print(IdBundesland)
        data_single_lk_neu = data_single_lk.loc[data_single_lk['MeldedatumISO'] == date]
        if data_single_lk_neu.empty:
            data_neu_ges = 0
        else:
            data_recovery(var_da_sort, var_da_anz)
        number_lk = file.removesuffix('.csv')
        print(f"{number_lk}")
        print(type(f"{number_lk}"))
        print(data_neu_ges)
        print(type(data_neu_ges))
        print(IdBundesland)
        print(type(IdBundesland))
        IdBundesland = int(IdBundesland)
        data_neu_ges = int(data_neu_ges)
        #fall_t = {f"{number_lk}", data_neu_ges, IdBundesland}
        fall_t = {f"{number_lk}", data_neu_ges, IdBundesland}
        print(fall_t)
        fall_t = list(fall_t)
        print(fall_t)
        print(type(fall_t))
        anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = fall_t


# ----------------------------------------------------------------------------------------------------------------------
# Daten auf relevante Ebene kürzen:
if ebene == 1:
    data_lk(anzfae_all_lk_1)

if ebene == 2:
    data_laender(var_da, anzfae_all_lk_1, laufvar_laender)

if ebene == 3:
    data_bund(var_da, anzfae_all_lk_1, date)

print(anzfae_all_lk)
print(type(anzfae_all_lk))
anzfae_all_lk_1.to_csv("hallowelt.csv")

# ----------------------------------------------------------------------------------------------------------------------
# letzte Zeile löschen:
if os.path.isfile(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\-1.csv"'):
    anzfae_all_lk = anzfae_all_lk_1.iloc[1:]
else:
    anzfae_all_lk = anzfae_all_lk_1

# ----------------------------------------------------------------------------------------------------------------------
# Map generieren und mit Daten kombinieren:

# import shapefile:
if ebene == 1:
    map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_KRS.shp")
    map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
    merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index('IdLandkreis'))

if ebene == 2:
    map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_LAN.shp")
    map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
    merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index("IdBundesland"))

if ebene == 3:
    map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_STA.shp")
    map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
    merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index("Bundesgebiet"))

# ----------------------------------------------------------------------------------------------------------------------
# 1) Auswahl der Spalte mit den relevanten Daten:
column = merged[f'{var_da}']

# 2) Auswahl des Maximums sowie Übertragen auf Legende rechts:
max_betroffene = column.max()
vmin, vmax = 0, max_betroffene

# 3) Auswahl der Daten aus Geometry sowie Schreiben in einzelne Spalte:
merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
merged['coords'] = [coords[0] for coords in merged['coords']]

# ----------------------------------------------------------------------------------------------------------------------
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# Hiermit werden NAN Werte auch angezeigt:
merged.plot(column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8',
            missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"})

# Die eigentliche Figure bauen:
for idx, row in merged.iterrows():
    if ebene == 2 and idx =='Berlin':
        plt.annotate(text=row['anz_erk'], xy=row['coords'],horizontalalignment='left',fontsize=8)
        continue
    plt.annotate(text=row[f'{var_da}'], xy=row['coords'],horizontalalignment='center',fontsize=8)
# remove the axis
ax.axis('off')
# add a title
ax.set_title(f'Coronavirus {var_da_verb} in Germany ({date})', fontdict={'fontsize': '18','fontweight' : '3'})
ax.annotate('Source: https://www.coronavirus.jetzt/karten/deutschland/',xy=(0.2, .06), xycoords='figure fraction'
            ,horizontalalignment='left', verticalalignment='top',fontsize=10, color='#555555')
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.savefig('testmap_1.png', dpi=300)

plt.show()