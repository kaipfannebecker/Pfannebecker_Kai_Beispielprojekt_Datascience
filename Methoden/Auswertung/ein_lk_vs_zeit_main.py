import matplotlib.pyplot as plt
import pandas as pd

import os
import logging
from datetime import datetime, timedelta, date
import sys


from Methoden.Auswertung.Helper import aktualitaet, gen_var, data_recovery, aufruf_lk, datumseingabe, sort_meld

today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Bestimmt über das Modul "aufruf_lk.py" genau einen Landkreis, prüft die Data_collection über das Module "aktualitaet.py" auf
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
# liste_lk = 1001

# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------


def main(ebene, datensatz):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    variablen = variablengeneration(ebene, datensatz)
    var_eb = variablen[0]
    var_da = variablen[1]
    var_da_anz = variablen[2]
    var_da_sort = variablen[3]
    var_da_verb = variablen[4]

    akt = 1  # to do !

    print("-------------------------------------------")
    print("Die notwendigen Variablen wurden generiert.")
    logger.info("Die Variablengeneration ist abgelaufen.")
    print("-------------------------------------------")

    lk_best_ret = lk_best()
    liste_lk = lk_best_ret[0]
    name_lk = lk_best_ret[1]
    print(name_lk)
    print("Der Landkreis wurde erfolgreich bestimmt.")
    logger.info(f'Landkreis bestimmen erfolgreich, die ID lautet: {liste_lk}')
    print("-------------------------------------------")

    akt = aktuali(akt)
    print("Der Datensatz  wurde erfolgreich aktualisiert.")
    logger.info(f'Der Datensatz  wurde erfolgreich aktualisiert, returncode: sort = {akt}')
    sort = sortieren(liste_lk)
    print("Der ausgewählte Datensatz wurde sortiert.")
    logger.info(f'Datensatz nach MeldedatumISO sortiert, returncode: sort = {sort}')
    print("-------------------------------------------")

    dataset = lk_einlesen(liste_lk)
    print("Der Landkreis wurde erfolgreich eingelesen.")
    logger.info(f'Der Landkreis wurde erfolgreich eingelesen.')
    print("-------------------------------------------")

    daten = define_dates()
    datestart = daten[0]
    dateend = daten[1]
    print(f"Start- und Enddatum wurde bestimmt.")
    logger.info(f'Das Startdatum ist {datestart}, das Enddatum {dateend}.')
    print("-------------------------------------------")

    dataset_final = datashortage(dataset, datestart, dateend)
    print("Der Datensatz wurde erfolgreich gekürzt.")
    logger.info("Der Datensatz wurde erfolgreich gekürzt.")
    print("-------------------------------------------")

    anzfae_lk_vs_t_1 = datacollection(ebene, dataset_final, var_da_anz, var_da_sort, datensatz)
    print("Die Data_collection wurden gesammelt.")
    logger.info("Die Data_collection wurden gesammelt.")
    print("-------------------------------------------")

    anzfae_lk_vs_t = add_dates_without_data(anzfae_lk_vs_t_1, datestart, dateend)
    lk_vs_t = sort_datum(anzfae_lk_vs_t)
    print("Der Datensatz wurde nach Datum sortiert.")
    logger.info("Der Datensatz wurde nach Datum sortiert.")
    print("-------------------------------------------")

    build_print_figure(lk_vs_t, liste_lk, var_da_sort, datensatz, name_lk)

# ----------------------------------------------------------------------------------------------------------------------


def define_dates():
    anz_dat = 2
    daten = datumseingabe.main(anz_dat)

    return daten


# ----------------------------------------------------------------------------------------------------------------------

def lk_best():
    # Gesuchten Landkreis abfragen
    aufruf_lk_ret = aufruf_lk.main()
    liste_lk = aufruf_lk_ret[0]
    name_lk = aufruf_lk_ret[1]
    #name_lk = name_lk_1[1]
    print(name_lk)
    #print(liste_lk)
    #print(type(liste_lk))
    liste_lk = str(liste_lk).replace('[', '').replace(']', '').replace("'", "")
    print(liste_lk)
    return liste_lk, name_lk

# ----------------------------------------------------------------------------------------------------------------------


# aktualitaet.py aufrufen und Aktualität der .csv Datei prüfen
def aktuali(akt):
    if akt <= 1:
        ausw_frag = eval(input(
            "Was möchten Sie tun? \n"
            "1) vorhandene Daten nutzen\n"
            "2) Daten aktualisieren\n"
            "3) Abbruch\n"
            ""
        ))

        if ausw_frag == 1:
            print("Die vorhandenen Daten werden genutzt")
        if ausw_frag == 2:
            akt = aktualitaet.main()
        if ausw_frag == 3:
            sys.exit()
    else:
        print("Keine Aktualisierung nötig, Auswertung geht weiter.")
    return akt


# ----------------------------------------------------------------------------------------------------------------------


# sort_meld.py aufrufen und Data_collection nach Meldedatum sortieren
def sortieren(liste_lk):
    anz_sort = 1
    zu_sort = liste_lk
    sort = sort_meld.main(zu_sort, anz_sort)
    return sort
# ----------------------------------------------------------------------------------------------------------------------


def lk_einlesen(liste_lk):
    # Aktuellen und sortierten Datensatz des Landkreises einlesen
    dataset = pd.read_csv(fr'.\rki_daten\Datensatz_vereinzelt\by_number\{liste_lk}.csv')
    return dataset
# ----------------------------------------------------------------------------------------------------------------------


def datashortage(dataset, datestart, dateend):

    # dataframe auf Start- und Enddatum kürzen:
    if datestart == today:
        dataset = dataset.sort_values(by="MeldedatumISO")
        dataset_short = dataset[dataset["MeldedatumISO"] >= datestart]

    else:
        dataset = dataset.sort_values(by="MeldedatumISO")
        dataset_short = dataset[dataset["MeldedatumISO"] >= datestart]

    if dateend == today:
        dataset_final = dataset_short
    else:
        dataset_short = dataset_short.sort_values(by="MeldedatumISO")
        dataset_final = dataset_short[dataset_short["MeldedatumISO"] <= dateend]

    return dataset_final

# ----------------------------------------------------------------------------------------------------------------------


def datacollection(ebene, dataset_final, var_da_anz, var_da_sort, datensatz):

    # erstellt den ursprünglichen Datensatz
    empty_df = {"Gesamtzahl neue Infektionen": [0], "Datum": [0], "IdBundesland": [0]}
    anzfae_lk_vs_t_1 = pd.DataFrame(data=empty_df)

    if datensatz == 1:
        pos_var_1 = "AnzahlTodesfall"
        pos_var_2 = "AnzahlGenesen"
        pos_anz_1 = "NeuerTodesfall"
        pos_anz_2 = "NeuGenesen"
    if datensatz == 2:
        pos_var_1 = "AnzahlTodesfall"
        pos_var_2 = "AnzahlFall"
        pos_anz_1 = "NeuerTodesfall"
        pos_anz_2 = "NeuerFall"
    if datensatz == 3:
        pos_var_1 = "AnzahlFall"
        pos_var_2 = "AnzahlGenesen"
        pos_anz_1 = "NeuerFall"
        pos_anz_2 = "NeuGenesen"

    ## iterieren über die einzelnen Data_collection von startdatum bis enddatum
    if ebene == 1:  # funktioniert!
        first_column_header = dataset_final.columns[0]
        for meld_dat, dataset_final in dataset_final.groupby('MeldedatumISO'):
            dataset_final = dataset_final.drop(
                columns=[f"{first_column_header}", "Landkreis", "Bundesland", "Altersgruppe2", "Altersgruppe",
                         "IdLandkreis", "IstErkrankungsbeginn", "DatenstandISO", "Geschlecht", f"{pos_var_2}",
                         f"{pos_var_1}", f"{pos_anz_1}", f"{pos_anz_2}"]
            )

            IdBundesland = str(dataset_final.iloc[0]['IdBundesland'])

            data_neu_ges = data_recovery.main(var_da_sort, var_da_anz, dataset_final)

            fall_t = pd.DataFrame({"Datum": [f"{meld_dat}"], "Gesamtzahl neue Infektionen": [data_neu_ges], "IdBundesland": [IdBundesland]})

            frames = [anzfae_lk_vs_t_1,fall_t]
            anzfae_lk_vs_t_1 = pd.concat(frames)

    if ebene == 2:
        for file in os.listdir(r"/rki_daten/Datensatz_vereinzelt/by_number"):
            if file.endswith(".csv"):
                data_single_lk = pd.read_csv(fr".\rki_daten\Datensatz_vereinzelt\by_number\{file}")
                #data_single_lk = pd.read_csv(fr"C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\Datensatz_vereinzelt\by_number\{file}")
                IdBundesland = data_single_lk.iloc[0]['IdBundesland']
                data_single_lk_neu = data_single_lk.loc[data_single_lk['MeldedatumISO'] == date]
                if data_single_lk_neu.empty:
                    data_neu_ges = 0
                else:
                    data_neu_ges = data_recovery.main(var_da_sort, var_da_anz, data_single_lk_neu)
                number_lk = file.removesuffix('.csv')
                IdBundesland = str(IdBundesland)
                data_neu_ges = int(data_neu_ges)
                fall_t = {f"{number_lk}", data_neu_ges, IdBundesland}
                fall_t = list(fall_t)
                anzfae_lk_vs_t_1.loc[len(anzfae_lk_vs_t_1)] = fall_t
        # anzfae_lk_vs_t_1 = anzfae_lk_vs_t_1.iloc[1:]

    anzfae_lk_vs_t_1 = anzfae_lk_vs_t_1.iloc[1:]

    return anzfae_lk_vs_t_1

# ----------------------------------------------------------------------------------------------------------------------



def sort_datum(anzfae_lk_vs_t):
    # sortieren von lk_vs_t nach Datum
    lk_vs_t = anzfae_lk_vs_t.values.tolist()
    lk_vs_t.sort(key=lambda datum: datum[1])
    return lk_vs_t

# ----------------------------------------------------------------------------------------------------------------------


def build_print_figure(lk_vs_t, liste_lk, var_da_sort, datensatz, name_lk):
    data_plot = pd.DataFrame(lk_vs_t)
    data_plot = data_plot.rename(columns={0: "Gesamtzahl neue Infektionen", 1: "Datum", 2: "IdBundesland"})
    x = data_plot["Datum"]
    y = data_plot["Gesamtzahl neue Infektionen"]

    #print(x)
    #print(type(x))
    #print(y)
    #print(type(y))

    if datensatz == 1:
        fig_ueb = "neu Infizierten"
    if datensatz == 2:
        fig_ueb = "neu Genesenen"
    if datensatz == 3:
        fig_ueb = "neuen hinzugekommenen Toten"


    # plot
    fig, ax = plt.subplots()
    fig.autofmt_xdate(rotation=45)

    ax.plot(x, y, linewidth=2.0)
    plt.xticks(x[::4])

    plt.title(f"Verlauf der {fig_ueb} je Tag für den Landkreis {name_lk}")
    ax.set_xlabel("Datum", fontsize=14)
    ax.set_ylabel(f"Anzahl der {fig_ueb}", color="black", fontsize=14)

    fig.savefig(f'Anzahl_Faelle_vs_Zeit_für_{name_lk}.png', dpi=200, pad_inches=5)
    plt.show()


    #fig, ax = plt.subplots(figsize=(10, 10))  # Create a figure containing a single axes.
    # ax.plot(anzfae_lk_vs_t[0], anzfae_lk_vs_t[1], color="black")  # Plot some data on the axes.
    # ax.plot(lk_vs_t[0], lk_vs_t[1], color="black")  # Plot some data on the axes.
    #ax.plot(x[0], y[0], color="black")  # Plot some data on the axes.
    # plt.xticks(lk_vs_t[1])
    #ax.set_xlabel("Datum", fontsize=14)
    #ax.set_ylabel(f"Anzahl {var_da_sort}", color="black", fontsize=14)
    #plt.show()
    #fig.savefig(f'Anzahl_Faelle_vs_Zeit_für_{liste_lk}.png', dpi=200, pad_inches=5)

# ----------------------------------------------------------------------------------------------------------------------


# Generieren des leeren Dataframes sowie der Parameter passend zur Eingabe:
def variablengeneration(ebene, datensatz):
    variablen = gen_var.main(ebene, datensatz)

    return variablen

# ----------------------------------------------------------------------------------------------------------------------

def add_dates_without_data(anzfae_lk_vs_t_1, datestart, dateend):
    # Fülle die Tage ein, bei denen keine neuen Werte gemeldet wurden:
    buis_dates = pd.bdate_range(start=datestart, end=dateend, inclusive="both")
    buis_dates_time = buis_dates.strftime('%Y-%m-%d') # , %r
    buis_dates_ser = pd.Series(dtype='float64')
    dates_meld = anzfae_lk_vs_t_1["Datum"]
    for i in buis_dates_time:
        i_ser = pd.Series(i)
        buis_dates_ser = pd.concat([buis_dates_ser, i_ser])

    set1, set2 = set(buis_dates_ser), set(dates_meld)
    dates_final = set1 - set2

    for i in dates_final:
        df = pd.DataFrame({"Gesamtzahl neue Infektionen": ["0"], "Datum": [i], "IdBundesland": ["NaN"]})  # maybe IdBundesland anpassen
        frames = [anzfae_lk_vs_t_1,df]
        anzfae_lk_vs_t_1 = pd.concat(frames)

    return anzfae_lk_vs_t_1