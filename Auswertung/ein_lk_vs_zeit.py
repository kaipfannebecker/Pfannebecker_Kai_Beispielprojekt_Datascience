import matplotlib.pyplot as plt
import pandas as pd

# ließt alle vorhandenen Landkreise ein
lk_gesamt = pd.read_csv(r'C:\Users\Kai\Desktop\Projekt_Datascience\Liste_der_Landkreise_fuer_Projekt.csv')

# fragt den gesuchten Landkreis ab.
lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben")

# Geünschten Landkreis laden, mglw. neue Eingabe einfordern
while
    try:
        dataset = pd.read_csv(f"{lk_gesucht}.csv")
        continue
    except pd.errors.EmptyDataError:
        print("Der Datensatz für den Landkreis ist nicht vorhanden. Meinten Sie möglicherweise folgenden Landkreis?")
        namen_lk = lk_gesamt["1"]
        print(f"Meinten Sie vielleicht {k for k in lk_gesamt if f'{lk_gesucht}' in k}?")
        weiter = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:"
                       "1. erneute Eingabe eines Landkreises"
                       "2. Programm beenden")
        if weiter == 2:
            quit()
        else:
            lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben")


# >>> [k for k in lst if 'ab' in k]
# ['ab', 'abc']

# Abfrage ob Datensatz aktuell
if lastdate == yesterday and lastaktfaelle != NaN:
    continue
else:
    # Daten aktualisieren und schleife neu durchlaufen

data_sort = dataset.sort_values("Meldedatum", ascending=False) # alternativ: [3]

datestart = input("Bitte das Startdatum im Format YYYY-MM-DD eingeben")

# überprüfen, ob Daten im ausgewählten Datensatz seit dem vorhanden sind.
# kalender einlesen und aktuell halten

if datestart <= data_sort("Meldedatum"):
    continue
else:
    input("Das gewünschte Startdatum ist nicht im Datensatz vorhanden. Bitte ein neues Startdatum eingeben.")

dateend = input("Bitte das Enddatum im Formaz YYYY-MM-DD eingeben")


if dateend == today:
    continue
else:
    # Datensatz auf Enddatum kürzen
    df[enddatum] = data_sort["Meldedatum"] >= dateend
    data_short = df.enddatum


# plot date vs. aktive fälle

date = dataset[Refdatum]
faelle = dataset[aktfaelle]

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([date], [faelle]);  # Plot some data on the axes.