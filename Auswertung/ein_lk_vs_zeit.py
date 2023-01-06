import matplotlib.pyplot as plt
import pandas as pd
import runpy
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
akt = 1
sort = 1


# ----------------------------------------------------------------------------------------------------------------------

# Variablen:
anz_lk = 1
#sort = 0
#akt = 0
# ----------------------------------------------------------------------------------------------------------------------

# Gesuchten Landkreis abfragen
runpy.run_module(mod_name="aufruf_lk", run_name= anz_lk) # , mod_name=f"{zu_akt}"

# aktualitaet.py aufrufen und Aktualität der .csv Datei prüfen

if akt <= 1:
   zu_akt = liste_lk
   runpy.run_module(mod_name="aktualitaet", run_name=f"{zu_akt}")
else:
    break

## sort_meld.py aufrufen und Daten nach Meldedatum sortieren

#if sort < 1:
#    zu_sort = liste_lk
#    runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")
#else:
    #break

# Aktuellen und sortierten Datensatz des Landkreises einlesen

dataset = pd.read_csv{f'{liste_lk}.csv'}

# Das gewünschte Startdatum abfragen

datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben")

# überprüfen, ob Daten im ausgewählten Datensatz vorhanden sind.
while True:
    if datestart in dataset[3] == True:
        break
    else:
        datestart = input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum im Format YYYY-MM-DD eingeben.")

# dataframe auf Startdatum kürzen

if datestart == today:
    break
else:
    dataset.startdatum = dataset.sort["Meldedatum"] <= datestart
    dataset_short = dataset.startdatum

# Enddatum abfragen und überprüfen

dateend = input("Bitte das Enddatum im Formaz YYYY-MM-DD eingeben")

while True:
    if dateend > datestart:
        break
    else:
        dataend = input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum eingeben.")

# Datensatz auf Enddatum kürzen

if dateend == today:
    dataset_final = dataset_short
    break
else:
    dataset_short.enddatum = dataset_short.sort["Meldedatum"] >= dateend
    dataset_final = dataset_short.enddatum

# TESTEN, TESTEN, TESTEN!

# erstellt den ursprünglichen Datensatz
anzfae_lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

## iterieren über die einzelnen Daten von startdatum bis enddatum

for meld_dat, dataset_final in dataset_final.groupby('Meldedatum'):
    data_neu = dataset_final.loc[[6] == 1]
    data_neu.sum([6])
    fall_t = {f"{meld_dat}",data_neu.sum([9])}
    anzfae_lk_vs_t = anzfae_lk_vs_t.append(fall_t, ignore_index=True)

# use datetime.weekday()
#delta = timedelta(days=1)
#d = datestart
#diff = 0
#weekend = set([5, 6])
#df = dataset_final
#while d <= dateend:
#    if d.weekday() not in weekend:
#        # in eigene Dataframes zwischenspeichern
#        data_d = df.loc[df[3] == d]
#        # neue Infektionen (d. h. alle Fälle mit ([6] == 1) zählen
#        # subset mit allen neuen Fällen erstellen
#        data_d_neu = data_d.loc[[6] == 1]
#        fall_t = {f"{d}",data_d_neu.sum([9])}
#        lk_vs_t = lk_vs_t.append(fall_t, ignore_index=True)


#        diff += 1
#    d += delta


# df.loc[df['column_name'] == some_value]

# sortieren von lk_vs_t nach Datum
lk_vs_t = lk_vs_t.sort("Datum")

# plot date vs. aktive fälle getestet und funktioniert
## lk_vs_t = [["2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06","2022-12-07"],[10, 12, 14, 11, 13]]
## wurde zum test verwendet

fig, ax = plt.subplots(figsize=(10,10))  # Create a figure containing a single axes.
ax.plot(anzfae_lk_vs_t[0], anzfae_lk_vs_t[1], color="black")# Plot some data on the axes.
ax.set_xlabel("Datum", fontsize=14)
ax.set_ylabel("Anzahl neue Fälle", color="black", fontsize=14)
plt.show()
fig.savefig(f'Anzahl_Faelle_vs_Zeit_für_{liste_lk}.png',dpi=200,pad_inches=5)




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

