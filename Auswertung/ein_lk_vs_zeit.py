import matplotlib.pyplot as plt
import pandas as pd
import logging
import aufruf_lk
import aktualitaet
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
# Logging:
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='a'
)

# ----------------------------------------------------------------------------------------------------------------------



## zu Testzwecken:
akt = 1
sort = 1
liste_lk = 1001

# ----------------------------------------------------------------------------------------------------------------------

# Variablen:

# sort = 0
# akt = 0
# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------
def main(ebene, datensatz):
    liste_lk = lk_best()
    print("-------------------------------------------")
    print("Der Landkreis wurde erfolgreich bestimmt.")
    print("-------------------------------------------")
    dataset = lk_einlesen(liste_lk)
    print("-------------------------------------------")
    print("Der Landkreis wurde erfolgreich eingelesen.")
    print("-------------------------------------------")
    datestart = startdatum(dataset)
    print("-------------------------------------------")
    print("Das Startdatum wurde bestimmt.")
    print("-------------------------------------------")
    dateend = enddatum(datestart)
    print("-------------------------------------------")
    print("Das Enddatum wurde bestimmt.")
    print("-------------------------------------------")
    dataset_final = datashortage(dataset, datestart, dateend)
    print("-------------------------------------------")
    print("Der Datensatz wurde erfolgreich gekürzt.")
    print("-------------------------------------------")
    anzfae_lk_vs_t = datacollection(dataset_final)
    print("-------------------------------------------")
    print("Die Daten wurden gesammelt.")
    print("-------------------------------------------")
    lk_vs_t = sort_datum(anzfae_lk_vs_t)
    print("-------------------------------------------")
    print("Der Datensatz wurde nach Datum sortiert.")
    print("-------------------------------------------")
    build_print_figure(lk_vs_t)

# ----------------------------------------------------------------------------------------------------------------------

def lk_best():
    # Gesuchten Landkreis abfragen
    anz_lk = 1
    liste_lk = aufruf_lk.main(anz_lk)
    return liste_lk



# aktualitaet.py aufrufen und Aktualität der .csv Datei prüfen

#if akt <= 1:
#   zu_akt = liste_lk
#   akt = aktualitaet.main(zu_akt)
#   # runpy.run_module(mod_name="aktualitaet", run_name=f"{zu_akt}")
#   subprocess.call(['./aktualitaet.py', zu_akt])
#else:
    #print("Keine Aktualisierung nötig")
#return akt



## sort_meld.py aufrufen und Daten nach Meldedatum sortieren

#if sort < 1:
#    zu_sort = liste_lk
#    runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")
#else:
    #break


def lk_einlesen(liste_lk):
    # Aktuellen und sortierten Datensatz des Landkreises einlesen
    dataset = pd.read_csv(f'C:\\Users\\Kai\\Documents\\GitHub\\Projekt_Datascience\\rki_daten\\Datensatz_vereinzelt\\by_number\\{liste_lk}.csv')
    return dataset

def startdatum(dataset):
    # Das gewünschte Startdatum abfragen und auf Vorhandensein überprüfen
    datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben ")
    datum = dataset["MeldedatumISO"].squeeze()

    # überprüfen, ob Daten im ausgewählten Datensatz vorhanden sind.
    while True:
        #if datestart in dataset["Meldedatum"] == True:
        if datestart in datum.values:
            print("Das gewünschte Startdatum ist im Datensatz vorhanden.")
            break
        else:
            datestart = input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum im Format YYYY-MM-DD eingeben. ")
    return datestart

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

# Enddatum abfragen und überprüfen
def enddatum(datestart):
    dateend = input("Bitte das Enddatum im Format YYYY-MM-DD eingeben ")

    while True:
        if dateend > datestart:
            print("Das gewünschte Startdatum liegt vor dem Enddatum")
            break
        else:
            dataend = input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum eingeben. ")
    return dateend

# Datensatz auf Enddatum kürzen

#if dateend == today:
#    dataset_final = dataset_short
#else:
 #   dataset_short = dataset_short.sort_values(by="MeldedatumISO")
  #  dataset_final = dataset_short[dataset_short["MeldedatumISO"] <= dateend]


def datacollection(dataset_final):
    # erstellt den ursprünglichen Datensatz
    empty_df = {"Gesamtzahl neue Infektionen": [0], "Datum": [0]}
    anzfae_lk_vs_t = pd.DataFrame(data=empty_df)

    ## iterieren über die einzelnen Daten von startdatum bis enddatum

    for meld_dat, dataset_final in dataset_final.groupby('MeldedatumISO'):
        dataset_final = dataset_final.drop(columns=["0", "Landkreis", "NeuerTodesfall", "NeuGenesen", "Bundesland",
                                                    "Altersgruppe2",  "Altersgruppe", "IdLandkreis", "IdBundesland",
                                                    "IstErkrankungsbeginn", "AnzahlTodesfall", "AnzahlGenesen"])
        data_neu_pos = dataset_final.loc[dataset_final['NeuerFall'] == 1.0]
        data_neu_pos = data_neu_pos.sum()
        data_neu_pos_num = data_neu_pos["AnzahlFall"]
        data_neu_neg = dataset_final.loc[dataset_final["NeuerFall"] == -1.0]
        if data_neu_neg.empty:
            data_neu_neg_num = 0
        else:
            data_neu_neg = data_neu_neg.sum()
            data_neu_neg_num = data_neu_neg["AnzahlFall"]
        data_neu_ges = data_neu_pos_num + data_neu_neg_num
        print(data_neu_ges)
        print(type(data_neu_ges))
        print(f"{meld_dat}")
        print(type(f"{meld_dat}"))
    #    fall_t = {f"{meld_dat}",data_neu_pos}
        fall_t = {f"{meld_dat}",data_neu_ges}
        fall_t = list(fall_t)
        print(fall_t)
        #print(type(fall_t))
        anzfae_lk_vs_t.loc[len(anzfae_lk_vs_t)] = fall_t

    anzfae_lk_vs_t = anzfae_lk_vs_t.iloc[1:]
    print(anzfae_lk_vs_t)
    print(type(anzfae_lk_vs_t))
        #anzfae_lk_vs_t = anzfae_lk_vs_t.append(fall_t, ignore_index=True)
    #print(anzfae_lk_vs_t)
    return anzfae_lk_vs_t

def sort_datum(anzfae_lk_vs_t):
    # sortieren von lk_vs_t nach Datum
    lk_vs_t = anzfae_lk_vs_t.values.tolist()
    print(lk_vs_t)
    return lk_vs_t
def build_print_figure(lk_vs_t):
    fig, ax = plt.subplots(figsize=(10,10))  # Create a figure containing a single axes.
    #ax.plot(anzfae_lk_vs_t[0], anzfae_lk_vs_t[1], color="black")# Plot some data on the axes.
    ax.plot(lk_vs_t[1], lk_vs_t[0], color="black")# Plot some data on the axes.
    #plt.xticks(lk_vs_t[1])
    ax.set_xlabel("Datum", fontsize=14)
    ax.set_ylabel("Anzahl neue Fälle", color="black", fontsize=14)
    plt.show()
    fig.savefig(f'Anzahl_Faelle_vs_Zeit_für_{liste_lk}.png',dpi=200,pad_inches=5)

# ----------------------------------------------------------------------------------------------------------------------

























## Alternative:
#for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
#    row_lk = tab_lk.loc[tab_lk["0"] == Id_lk]
#    number_lk = row_lk['0'].values[0]
#    # name_lk = row_lk['1'].values[0]
#    ## save the dataframe for each group to a csv; seperated for each Landkreis
#    # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk}.csv', index=False, mode='a')
#    dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\{number_lk}.csv', index=False, mode='a')








# >>> [k for k in lst if 'ab' in k]
# ['ab', 'abc']

######### example.py ########
# print("I am an example")

######### run_example.py ########
# import runpy

# runpy.run_module(mod_name="example")  # to run module example.py

## -> I am an example

# The head() method on DataFrame can give you the first n rows of a DataFrame.
# Indexing of a DataFrame will allow you to select rows meeting your filter criteria
# - to narrow to a subset DataFrame with such rows. Together, you could use them to do:

# r = df.loc[df.ok == 'x', :].head(1)

# What you are doing here is narrowing to a subset DataFrame where ok is 'x'
# (the df.loc[df.ok == 'x', :] part), then taking the first row of it (the .head(1) part).
# This of course assumes the DataFrame is sorted by date as it is above.

