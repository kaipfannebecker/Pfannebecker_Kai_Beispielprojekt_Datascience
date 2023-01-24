import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

import logging
import os
import sys

import datumseingabe
import aktualitaet
import gen_var

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Daten über das Module "aktualitaet.py" auf
## Aktualität und sortiert über "sort_meld.py" nach Meldedatum. Danach wird das Startdatum sowie Enddatum bestimmt und
## die Zahl der resultierenden Fälle pro Tag als Graph ausgegeben.

# Benötigt:
## "aufruf_lk.py"
## "aktualitaet.py"
## "sort_meld.py"
## "datumseingabe.py"

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
#data_neu_ges = 0
#global anz_date
#anz_date = 1


# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------

# Main function:
def main(ebene, datensatz):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
               'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    variablen = variablengeneration(ebene, datensatz)
    var_eb = variablen[0]
    var_da = variablen[1]
    var_da_anz = variablen[2]
    var_da_sort = variablen[3]
    var_da_verb = variablen[4]
    print("-------------------------------------------")
    print("Die notwendigen Variablen wurden generiert.")
    logger.info("Die Variablengeneration ist abgelaufen.")
    print("----------------------------")

    date = datumsabfrage()
    print(f"Das gewünschte Datum ist {date}")
    logger.info(f"Die Datumsabfrage ist abgelaufen, das gewünschte Datum ist {date}")
    print("----------------------------")

    date = datumspruefung(date)
    print("Das gewünschte Datum ist vorhanden.")
    logger.info("Die Datumsprüfung ist abgelaufen. Das gewünschte Datum ist vorhanden.")
    print("----------------------------")

    datacolvar = datacollection(date, var_da, var_da_sort, var_da_anz)
    anzfae_all_lk_1 = datacolvar[0]
    berlin_bez_1 = datacolvar[1]
    print("Die Daten wurden gesammelt.")
    logger.info("Die Daten wurden gesammelt.")
    print("----------------------------")

    dateshortvar = datashortage(ebene, anzfae_all_lk_1, var_da, var_da_anz, berlin_bez_1)
    anzfae_all_lk = dateshortvar[0]
    berlin_bez = dateshortvar[1]
    print("Die Daten wurden auf den gewünschten Zeitraum gekürzt.")
    logger.info("Die Daten wurden auf den gewünschten Zeitraum gekürzt.")
    print("----------------------------")

    mapgen = mapgeneration(ebene, anzfae_all_lk, var_da, berlin_bez)
    merged = mapgen[0]
    vmin = mapgen[1]
    vmax = mapgen[2]
    merged_add = mapgen[3]
    merged_berlin = mapgen[4]
    print("Die Karte wurde erstellt.")
    logger.info("Die Karte wurde erstellt.")
    print("----------------------------")

    createfigure(merged, var_da, var_da_verb, date, vmin, vmax, merged_add, merged_berlin, ebene)

# ----------------------------------------------------------------------------------------------------------------------
################################################# Definierte Funktionen ################################################
# ----------------------------------------------------------------------------------------------------------------------

# gibt das DAtum der zuletzt eingelesenen Quelldatei mit Coronarohdaten aus:
def data_test():
    with open(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\urls_used.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        global date_dataset
        date_dataset = last_line[82:92]


# ----------------------------------------------------------------------------------------------------------------------

# Sammelt die relevanten Anzahlen der Daten je nach gewünschter Ebene und Datensatz
def data_recovery(var_da_sort, var_da_anz, data_single_lk_neu):
    data_neu_pos_1 = data_single_lk_neu.loc[data_single_lk_neu[f'{var_da_sort}'] == 1.0]
    data_neu_pos = data_neu_pos_1.sum()
    data_neu_pos_num = data_neu_pos[f"{var_da_anz}"]
    data_neu_neg_1 = data_single_lk_neu.loc[data_single_lk_neu[f"{var_da_sort}"] == -1.0]
    if data_neu_neg_1.empty:
        data_neu_neg_num = 0
    else:
        data_neu_neg = data_neu_neg_1.sum()
        data_neu_neg_num = data_neu_neg[f"{var_da_anz}"]
    data_neu_ges = data_neu_pos_num + data_neu_neg_num
    return data_neu_ges


# ----------------------------------------------------------------------------------------------------------------------


def data_lk(anzfae_all_lk_1):
    anzfae_all_lk_1['IdLandkreis'] = anzfae_all_lk_1['IdLandkreis'].astype(str)
    for index in anzfae_all_lk_1:
        anzfae_all_lk_1['IdLandkreis'] = anzfae_all_lk_1['IdLandkreis'].str.zfill(5)
    return anzfae_all_lk_1

# ----------------------------------------------------------------------------------------------------------------------


def data_laender(var_da, anzfae_all_lk_1):
    laufvar_laender = 1
    dataset_empt = {"IdBundesland": [], var_da: []}
    # Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
    dataset = pd.DataFrame(data=dataset_empt)
    while laufvar_laender < 17:
        anzfae_all_lk_neu_1 = anzfae_all_lk_1.loc[anzfae_all_lk_1['IdBundesland'] == laufvar_laender]
        anzfae_all_lk_neu = anzfae_all_lk_neu_1.sum()

        bula_data_2 = {f"{var_da}": anzfae_all_lk_neu[f"{var_da}"], 'IdBundesland': laufvar_laender}  # hier noch
        bula_data_1 = pd.Series(bula_data_2, name=f"{var_da}")  # Optimierungsmöglichkeiten
        bula_data_1.reset_index()
        bula_data = bula_data_1.to_frame()
        bula_data = bula_data.transpose()
        frame_data = [dataset, bula_data]
        dataset = pd.concat(frame_data)
        laufvar_laender = laufvar_laender + 1

    anzfae_all_lk_1 = dataset.reset_index(drop=True)
    # ------------------------------------------------------------------------------------------------------------------
    anzfae_all_lk_1['IdBundesland'] = anzfae_all_lk_1['IdBundesland'].astype(int)
    anzfae_all_lk_1['IdBundesland'] = anzfae_all_lk_1['IdBundesland'].astype(str)
    for index in anzfae_all_lk_1:
        anzfae_all_lk_1['IdBundesland'] = anzfae_all_lk_1['IdBundesland'].str.zfill(2)
    # ------------------------------------------------------------------------------------------------------------------

    return anzfae_all_lk_1

# ----------------------------------------------------------------------------------------------------------------------


def data_bund(var_da, anzfae_all_lk_1, var_da_anz):
    dataset_empt = {var_da: [0], "Bundesgebiet": "Bundesgebiet"}
    # Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
    dataset = pd.DataFrame(data=dataset_empt)
    anzfae_all_lk_neu = anzfae_all_lk_1.sum()
    anzfae_all_lk_neu_ges = anzfae_all_lk_neu[f"{var_da_anz}"]
    dataset = {anzfae_all_lk_neu_ges, "Bundesgebiet"}
    dataset = list(dataset)
    anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = dataset

    # ---------------------------------
    # berlin_bez_empt = {"Gesamtzahl neue Infektionen": [0], "IdLandkreis": [0], "IdBundesland": [0]}
    # berlin_bez_1 = pd.DataFrame(data=berlin_bez_empt)
    # frame_mitt = [berlin_bez_1, berlin_mitt]
    # berlin_bez_1 = pd.concat(frame_mitt)
    # -------------------------------------------

    return anzfae_all_lk_1

# ----------------------------------------------------------------------------------------------------------------------
# Gesuchtes Datum abfragen


def datumsabfrage():
    date = datumseingabe.eindatum()
    return date

# ----------------------------------------------------------------------------------------------------------------------
# Prüfen ob gewünschtes Datum im Datensatz vorhanden ist:


def datumspruefung(date):
    data_test()
    if date_dataset > date or date_dataset == date:
        print("Das gewünschte Datum ist im Datensatz vorhanden.")
    if date_dataset < date:
        entscheidung = eval(input(
            "Das gewünschte Datum ist nicht im Datensatz vorhanden. Sie können nun entweder:"
            "1) Ein neues Datum eingeben"
            "2) Den Datensatz aktualisieren"
            "3) Den Vorgang abbrechen "
        ))
        if entscheidung == 1:
            date = datumseingabe.eindatum()
        if entscheidung == 2:
            #aktualitaet.eindatum()
            #date = datumseingabe.datum
            data_test()
        if entscheidung == 3:
            sys.exit()
    return date
# ----------------------------------------------------------------------------------------------------------------------


# Generieren des leeren Dataframes sowie der Parameter passend zur Eingabe:
def variablengeneration(ebene, datensatz):

    variablen = gen_var.main(ebene, datensatz)
    var_eb = variablen[0]
    var_da = variablen[1]
    var_da_anz = variablen[2]
    var_da_sort = variablen[3]
    var_da_verb = variablen[4]

    return var_eb, var_da, var_da_anz, var_da_sort, var_da_verb

# ----------------------------------------------------------------------------------------------------------------------


# Daten vom gewünschten Tag aus allen Landkreisen abfragen:
def datacollection(date, var_da, var_da_sort, var_da_anz):
    empty_df = {var_da: [0], "IdLandkreis": [0], "IdBundesland": [0]}
    # Beispiel: Alle todesfälle auf Landkreisebene: {"Gesamtzahl neue Todesfälle": [0], IdLandkreis: [0]}
    anzfae_all_lk_1 = pd.DataFrame(data=empty_df)

    # ------------------------------------------------------------------------------------------------------------------

    for file in os.listdir(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number"):

        if file.endswith(".csv"):
            data_single_lk = pd.read_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{file}")
            id_bundesland = data_single_lk.iloc[0]['IdBundesland']
            data_single_lk_neu = data_single_lk.loc[data_single_lk['MeldedatumISO'] == date]
            if data_single_lk_neu.empty:
                data_neu_ges = 0
            else:
                data_neu_ges = data_recovery(var_da_sort, var_da_anz, data_single_lk_neu)
            number_lk = file.removesuffix('.csv')
            id_bundesland = int(id_bundesland)
            data_neu_ges = int(data_neu_ges)
            fall_t = pd.DataFrame({var_da: [data_neu_ges], "IdLandkreis": [f"{number_lk}"],
                                   "IdBundesland": [id_bundesland]})
            frames = [anzfae_all_lk_1, fall_t]
            anzfae_all_lk_1 = pd.concat(frames)

    # ------------------------------------------------------------------------------------------------------------------

    # Die einzelnen Datenpunkte für Berlin bestimmen und zusammenrechnen:
    # ------------------------------------------------------------------------------------------------------------------
    x = ["11001", "11002", "11003", "11004", "11005", "11006", "11007", "11008", "11009", "11010", "11011", "11012"]
    y = ["11000001", "11000002", "11000003", "11000004", "11000005", "11000006", "11000007", "11000008", "11000009", "11000010", "11000011", "11000012"]
    print(x)
    print(type(x))

    berlin_bez_empt = {f"{var_da}": [0], "IdLandkreis": [0], "IdBundesland": [0]}
    berlin_bez_1 = pd.DataFrame(data=berlin_bez_empt)
    berlin_spez_bez_var = {}

    for i in range(0, 12):
        x1 = x[i]
        y1 = y[i]
        berlin_spez_bez = anzfae_all_lk_1.loc[anzfae_all_lk_1["IdLandkreis"] == x1]
        print(berlin_spez_bez)
        print(y1)
        berlin_spez_bez_var[i] = berlin_spez_bez[f"{var_da}"].iloc[0]
        berlin_spez_bez.loc[0, 'IdLandkreis'] = y1
        frame_bez = [berlin_bez_1, berlin_spez_bez]
        berlin_bez_1 = pd.concat(frame_bez)

    print(berlin_bez_1)

    berlin_gesamt = (
            berlin_spez_bez_var[0] + berlin_spez_bez_var[1] + berlin_spez_bez_var[2] + berlin_spez_bez_var[3] +
            berlin_spez_bez_var[4] + berlin_spez_bez_var[5] + berlin_spez_bez_var[6] + berlin_spez_bez_var[7] +
            berlin_spez_bez_var[8] + berlin_spez_bez_var[9] + berlin_spez_bez_var[10] + berlin_spez_bez_var[11]
    )

    fall_t = pd.DataFrame({var_da: [berlin_gesamt], "IdLandkreis": ["11000"], "IdBundesland": [11]})
    frames = [anzfae_all_lk_1, fall_t]
    anzfae_all_lk_1 = pd.concat(frames)

    # ------------------------------------------------------------------------------------------------------------------

    return anzfae_all_lk_1, berlin_bez_1

# data_neu_pos_1 = data_single_lk_neu.loc[data_single_lk_neu[f'{var_da_sort}'] == 1.0]
    # fall_t = pd.DataFrame({"Datum": [f"{meld_dat}"], "Gesamtzahl neue Infektionen": [data_neu_ges], "IdBundesland": [IdBundesland]})
    # frames = [anzfae_lk_vs_t_1,fall_t]
    # anzfae_lk_vs_t_1 = pd.concat(frames)

    # fall_t = {f"{number_lk}", data_neu_ges, IdBundesland}
    # fall_t = list(fall_t)
    # anzfae_all_lk_1.loc[len(anzfae_all_lk_1)] = fall_t

# ----------------------------------------------------------------------------------------------------------------------


# Daten auf relevante Ebene kürzen und bearbeiten:
def datashortage(ebene, anzfae_all_lk_1, var_da, var_da_anz, berlin_bez_1):
    if ebene == 1:
        anzfae_all_lk_1 = data_lk(anzfae_all_lk_1)
        berlin_bez_1 = data_lk(berlin_bez_1)

    if ebene == 2:
        anzfae_all_lk_1 = data_laender(var_da, anzfae_all_lk_1)

    if ebene == 3:
        anzfae_all_lk_1 = data_bund(var_da, anzfae_all_lk_1, var_da_anz)  # , date

    # ------------------------------------------------------------------------------------------------------------------
    # erste Zeile mglw. löschen:
    if os.path.isfile(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\-1.csv"'):
        anzfae_all_lk = anzfae_all_lk_1.iloc[1:]
        berlin_bez = berlin_bez_1.iloc[1:]
    else:
        anzfae_all_lk = anzfae_all_lk_1
        berlin_bez = berlin_bez_1
    return anzfae_all_lk, berlin_bez
# ----------------------------------------------------------------------------------------------------------------------


# Map generieren und mit Daten kombinieren:
def mapgeneration(ebene, anzfae_all_lk, var_da, berlin_bez):
    # import shapefile:
    if ebene == 1:
        map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_KRS.shp")
        map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
        merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index('IdLandkreis'))

        # zusätzlich Grenzen Bundesländer verstärken:
        map_lk_add = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_LAN.shp")
        map_lk_add_eind = map_lk_add.loc[map_lk['GF'] == 9]
        merged_add = map_lk_add_eind.set_index('AGS').join(anzfae_all_lk.set_index("IdLandkreis"))

        # Berlin extra ausweisen:
        karte_berlin = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\bezirksgrenzen.geojson")
        merged_berlin = karte_berlin.set_index('Schluessel_gesamt').join(berlin_bez.set_index("IdLandkreis"))

        merged_berlin['coords'] = merged_berlin['geometry'].apply(lambda x: x.representative_point().coords[:])
        merged_berlin['coords'] = [coords[0] for coords in merged_berlin['coords']]

    if ebene == 2:
        map_lk = gpd.read_file(r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_LAN.shp")
        map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
        merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index("IdBundesland"))
        merged_add = ()
        merged_berlin = ()

    if ebene == 3:
        map_lk = gpd.read_file(
            r"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\Geoshape_Deutschland_vg2500_12-31.utm32s.shape\vg2500\VG2500_STA.shp"
        )
        map_lk_eind = map_lk.loc[map_lk['GF'] == 9]
        merged = map_lk_eind.set_index('AGS').join(anzfae_all_lk.set_index("Bundesgebiet"))
        merged_add = ()
        merged_berlin = ()

    # 1) Auswahl der Spalte mit den relevanten Daten:
    column = merged[f'{var_da}']

    # 2) Auswahl des Maximums sowie Übertragen auf Legende rechts:
    max_betroffene = column.max()
    vmin, vmax = 0, max_betroffene

    # 3) Auswahl der Daten aus Geometry sowie Schreiben in einzelne Spalte:
    merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
    merged['coords'] = [coords[0] for coords in merged['coords']]

    return merged, vmin, vmax, merged_add, merged_berlin

# ----------------------------------------------------------------------------------------------------------------------


def createfigure(merged, var_da, var_da_verb, date, vmin, vmax, merged_add, merged_berlin, ebene):

# to do_build subplot with merged_berlin

    # create figure and axes for Matplotlib
    # fig, ax = plt.subplots(1, figsize=(10, 6))

    # fig, [[ax1, ax2]] = plt.subplots(nrows=1, ncols=2, squeeze=False)  # figsize=(10, 6)

   # # Hiermit werden NAN Werte auch angezeigt:
   # merged.plot(column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8',
    #            missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"})

    # Hiermit werden NAN Werte auch angezeigt:
    # missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"}

    # Grenzen Landkreise ausweisen:
    # merged.plot(ax=ax1, column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, edgecolor='0.8',
     #           missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"}, alpha=0.5)

    if ebene == 1:
        # create figure and axes for Matplotlib
        fig, [[ax1, ax2]] = plt.subplots(nrows=1, ncols=2, squeeze=False)  # figsize=(10, 6)
        # Grenzen Landkreise ausweisen:
        merged.plot(
            ax=ax1, column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, edgecolor='0.8',
            missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"}, alpha=0.5
        )

        # Grenzen Bundesländer stärker hervorheben:
        merged_add.plot(facecolor="none", linewidth=0.8, ax=ax1, edgecolor='k')  # , missing_kwds={"edgecolor": "k"}

        # Subfigure Berlin definieren:
        merged_berlin.plot(
            ax=ax2, column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, edgecolor='0.8',
            missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"}
        )  # , alpha=0.5

        # Bildüberschriften
        ax1.set_title(f'Coronavirus {var_da_verb} in Germany ({date})', fontdict={'fontsize': '18','fontweight': '3'})
        ax2.set_title(f'Coronavirus {var_da_verb} in Berlin ({date})', fontdict={'fontsize': '18','fontweight': '3'})

        # Achsen entfernen:
        ax1.axis('off')
        ax2.axis('off')

        # Bildunterschriften:
        ax1.annotate(
            'Datenquelle: RKI',xy=(0.2, .06), xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=10, color='#555555'
        )

    if ebene == 2:
        # create figure and axes for Matplotlib
        fig, ax = plt.subplots(1, figsize=(10, 6))

        # Grenzen Bundesländer ausweisen:
        merged.plot(ax=ax, column=f'{var_da}', cmap='YlOrRd', linewidth=0.8, edgecolor='0.8',
                    missing_kwds={"color": "darkgrey", "edgecolor": "k", "label": "Missing values"})  # , alpha=0.5

        # Bildüberschriften
        ax.set_title(f'Coronavirus {var_da_verb} in Germany ({date})', fontdict={'fontsize': '18', 'fontweight': '3'})

        # Achsen entfernen:
        ax.axis('off')

        # Bildunterschriften:
        ax.annotate(
            'Datenquelle: RKI',xy=(0.2, .06), xycoords='figure fraction', horizontalalignment='center',
            verticalalignment='top', fontsize=10, color='#555555'
        )


    # Die eigentliche Figure bauen:

    # Diese Reihe erzeugt die Nummern auf der Karte:
    #for idx, row in merged.iterrows():
        #plt.annotate(text=row[f'{var_da}'], xy=row['coords'],horizontalalignment='center',fontsize=8)


    sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    cbar = fig.colorbar(sm)
    fig.savefig('testmap_1.png', dpi=300)

#    manager = plt.get_current_fig_manager()
    #figManager = plt.get_current_fig_manager()
    #figManager.window.showMaximized()
    # manager.full_screen_toggle()
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')

    plt.show()

# ----------------------------------------------------------------------------------------------------------------------
