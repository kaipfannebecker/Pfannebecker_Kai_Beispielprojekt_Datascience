import matplotlib.pyplot as plt
import pandas as pd
import runpy

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
        continue
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

for True == True:
    if datestart in lk_gesucht[3] == True:
        continue
    else:
        datestart = input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum eingeben.")

# dataframe auf Startdatum kürzen

if dateend == today:
    continue
else:
    lk_gesucht[startdatum] = lk_gesucht.sort["Meldedatum"] <= datestart
    lk_gesucht_short = lk_gesucht.startdatum

# Enddatum abfragen und überprüfen

dateend = input("Bitte das Enddatum im Formaz YYYY-MM-DD eingeben")

for True == True:
    if dateend > datestart:
        continue
    else:
        dataend = input("Das gewünschte Enddatum liegt vor dem Startdatum. Bitte ein neues Enddatum eingeben.")

# Datensatz auf Enddatum kürzen

if dateend == today:
    continue
else:
    lk_gesucht_short[enddatum] = lk_gesucht_short.sort["Meldedatum"] >= dateend
    lk_gesucht_final = lk_gesucht_short.enddatum

# TESTEN, TESTEN, TESTEN!


# plot date vs. aktive fälle

# date = dataset[Refdatum]
# faelle = dataset[aktfaelle]

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([date], [faelle]);  # Plot some data on the axes.




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

