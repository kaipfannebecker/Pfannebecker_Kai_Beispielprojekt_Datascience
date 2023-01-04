import matplotlib.pyplot as plt
import pandas as pd
import runpy

from datetime import datetime # notwendig für Kalender

anz_lk = 1

# Gesuchten Landkreis abfragen
runpy.run_module(mod_name="aufruf_lk"; mod_name=anz_lk) # , mod_name=f"{zu_akt}"




datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben")

# überprüfen, ob Daten im ausgewählten Datensatz vorhanden sind.
while True == True:
    if datestart in dataset[3] == True:
        break
    else:
        datestart = input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum im Format YYYY-MM-DD eingeben.")

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
    dataset_final = dataset_short
    break
else:
    dataset_short[enddatum] = dataset_short.sort["Meldedatum"] >= dateend
    dataset_final = dataset_short.enddatum

# TESTEN, TESTEN, TESTEN!

# erstellt den ursprünglichen Datensatz
lk_vs_t = ["Datum", "Gesamtzahl neue Infektionen"]

## iterieren über die einzelnen Daten von startdatum bis enddatum

for meld_dat, dataset_final in dataset_final.groupby('Meldedatum'):
    data_neu = dataset_final.loc[[6] == 1]
    data_neu.sum([6])
    fall_t = {f"{d}",data_d_neu.sum([9])}
    lk_vs_t = lk_vs_t.append(fall_t, ignore_index=True)

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

# plot date vs. aktive fälle

date = lk_vs_t[0]
faelle = lk_vs_t[1]

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([date], [faelle]);  # Plot some data on the axes.

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

