import matplotlib.pyplot as plt
import pandas as pd
import runpy

from datetime import datetime # notwendig für Kalender

akt = 0
sort = 0

# ließt alle vorhandenen Landkreise ein
lk_gesamt = pd.read_csv(r'C:\Users\Kai\Desktop\Projekt_Datascience\Liste_der_Landkreise_fuer_Projekt.csv')

# fragt den gesuchten Landkreis ab.
lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben")

# Gewünschten Landkreis laden, mglw. neue Eingabe einfordern
while True == True:
    try:
        dataset = pd.read_csv(f"{lk_gesucht}.csv")
        break
    except pd.errors.EmptyDataError:
        print("Der Datensatz für den Landkreis ist nicht vorhanden. Meinten Sie möglicherweise folgenden Landkreis?")
        namen_lk = lk_gesamt["1"]
        #alt_lk = k for k in lk_gesamt if f'{lk_gesucht}' in k
        alt_lk = {k for k in namen_lk if f'{lk_gesucht}' in k}
        print(f"Meinten Sie vielleicht {alt_lk}?")
        weiter = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:"
                       "1. erneute Eingabe eines Landkreises"
                       "2. Programm beenden")
        if weiter == 2:
            quit()
        else:
            lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben")


# aktualitaet.py aufrufen und Aktualität der .csv Datei prüfen

for akt < 1:
    zu_akt = lk_gesucht
    runpy.run_module(mod_name="aktualitat", mod_name=f"{zu_akt}")

# sort_meld.py aufrufen und Daten nach Meldedatum sortieren
for sort < 1:
    zu_sort = lk_gesucht
    runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")

datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben")

# überprüfen, ob Daten im ausgewählten Datensatz vorhanden sind.
while True == True:
    if datestart in dataset[3] == True:
        break
    else:
        datestart = input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum eingeben.")

# dataframe auf Startdatum kürzen

if dateend == today:
    break
else:
    dataset[startdatum] = dataset.sort["Meldedatum"] <= datestart
    dataset_short = dataset.startdatum

# Enddatum abfragen und überprüfen

dateend = input("Bitte das Enddatum im Formaz YYYY-MM-DD eingeben")

for True == True:
    if dateend > datestart:
        break
    else:
        dataend = input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum eingeben.")

# Datensatz auf Enddatum kürzen

if dateend == today:
    break
else:
    dataset_short[enddatum] = dataset_short.sort["Meldedatum"] >= dateend
    dataset_final = dataset_short.enddatum

# TESTEN, TESTEN, TESTEN!

# erstellt den ursprünglichen Datensatz
lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

## iterieren über die einzelnen Daten von startdatum bis enddatum
# use datetime.weekday()
delta = timedelta(days=1)
d = datestart
diff = 0
weekend = set([5, 6])
df = dataset_final
while d <= dateend:
    if d.weekday() not in weekend:
        # in eigene Dataframes zwischenspeichern
        data_d = df.loc[df[3] == d]
        # neue Infektionen (d. h. alle Fälle mit ([6] == 1) zählen
        # subset mit allen neuen Fällen erstellen
        data_d_neu = data_d.loc[[6] == 1]
        fall_t = {f"{d}",data_d_neu.sum([9])}
        lk_vs_t = lk_vs_t.append(fall_t, ignore_index=True)


        diff += 1
    d += delta

# df.loc[df['column_name'] == some_value]

# sortieren von lk_vs_t nach Datum
lk_vs_t = lk_vs_t.sort("Datum")

# plot date vs. aktive fälle

date = lk_vs_t[0]
faelle = lk_vs_t[1]

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([date], [faelle]);  # Plot some data on the axes.




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

