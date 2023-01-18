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
anzfae_all_lk_1 = pd.DataFrame(data=empty_df)

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

# Einlesen von Daten funktioniert

# ----------------------------------------------------------------------------------------------------------------------
# letzte Zeile löschen, funktioniert noch nicht

anzfae_all_lk = anzfae_all_lk_1.iloc[1:]
anzfae_all_lk['IdLandkreis'] = anzfae_all_lk['IdLandkreis'].astype(str)
for index in anzfae_all_lk:
    anzfae_all_lk['IdLandkreis'] = anzfae_all_lk['IdLandkreis'].str.zfill(5)
print(anzfae_all_lk)
print(type(anzfae_all_lk))
anzfae_all_lk.to_csv("hallowelt.csv")
# ----------------------------------------------------------------------------------------------------------------------

# Zu testzwecken:
#df = {"Bundesland": ["Bayern", "Berlin", "Sachsen", "Thüringen","Sachsen-Anhalt", "Schleswig-Holstein", "Hessen", "RLP",
  #                   "Saarland", "Ba-Wü", "Niedersachsen", "Brandenburg", "Mecklenburg-Vorpommern", "Bremen", "Hamburg",
   #                  "Nordrhein-Westfalen"], "anz_erk": [10, 15, 20, 12, 10, 15, 20, 12, 10, 15, 20, 12, 10, 15, 20, 12]}
#anzfae_all_lk = pd.DataFrame(data=df)
#print(type(anzfae_all_lk))
#print(anzfae_all_lk)


# ----------------------------------------------------------------------------------------------------------------------
# Generating Map:

# import shapefile:
map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_KRS.shp")

map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
#data = pd.DataFrame(map_lk)


#import1 = map_lk_eind["AGS"]
#print(import1)
#import2 = anzfae_all_lk['IdLandkreis']
#print(import2)
# ----------------------------------------------------------------------------------------------------------------------
# Daten von Map und Datensatz kombinieren:
merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index('IdLandkreis'))

# ----------------------------------------------------------------------------------------------------------------------
# Generating plot:

# 1) Auswahl der Spalte mit den relevanten Daten:
column = merged['Gesamtzahl neue Infektionen']

# 2) Auswahl des Maximums sowie Übertragen auf Legende rechts:
max_Infizierte = column.max()
vmin, vmax = 0, max_Infizierte

# 3) Auswahl der Daten aus Geometry sowie Schreiben in einzelne Spalte:
merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
merged['coords'] = [coords[0] for coords in merged['coords']]

# ----------------------------------------------------------------------------------------------------------------------
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# Hiermit werden NAN Werte auch angezeigt:
merged.plot(column='Gesamtzahl neue Infektionen', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', missing_kwds={"color": "darkgrey",
                                                                                                 "edgecolor": "k", "label": "Missing values"})
# Die eigentliche Figure bauen:
for idx, row in merged.iterrows():
#    if idx =='Berlin':
#        plt.annotate(text=row['anz_erk'], xy=row['coords'],horizontalalignment='left',fontsize=8)
#        continue
    plt.annotate(text=row['Gesamtzahl neue Infektionen'], xy=row['coords'],horizontalalignment='center',fontsize=8)
# remove the axis
ax.axis('off')
# add a title
ax.set_title(f'Coronavirus infected in Germany ({date})', fontdict={'fontsize': '18','fontweight' : '3'})
ax.annotate('Source: https://www.coronavirus.jetzt/karten/deutschland/',xy=(0.2, .06), xycoords='figure fraction'
            ,horizontalalignment='left', verticalalignment='top',fontsize=10, color='#555555')
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.savefig('testmap_1.png', dpi=300)




#map_lk_eind.plot()
plt.show()




