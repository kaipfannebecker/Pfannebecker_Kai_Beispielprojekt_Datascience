import pandas as pd
import runpy

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Ruft "anz_lk" Landkreise ab, prüft diese über das Submodul aktualitaet.py auf Aktualität
## und gibt die Liste der Landkreise "liste_lk" zurück

# Benötigt:
## Übergabe von Variable anz_lk; gibt Anzahl der insgesamt gewünschten Landkreise an

# Gibt zurück:
## liste_lk = Liste der Landkreise

# ----------------------------------------------------------------------------------------------------------------------

## zu Testzwecken:
akt = 1
# sort = 1
anz_lk=2

# ----------------------------------------------------------------------------------------------------------------------

# ließt alle vorhandenen Landkreise ein
lk_gesamt = pd.read_csv(r'../Liste_der_Landkreise_fuer_Projekt.csv') #C:/Users/Kai/Desktop/Projekt_Datascience

i = 0

while i < anz_lk:
    print(i)
    print(anz_lk)
    # fragt den gesuchten Landkreis ab.
    lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")

    # Falls der Name des Landkreises eingegeben wird, diesen zur zugehörigen Nummer zurordnen
    if lk_gesucht.isalpha():
        reihe_ges = lk_gesamt.loc[lk_gesamt['1'] == "lk_gesucht"]
        lk_gesucht = reihe_ges[0]
    #elif lk_gesucht.isdigit():
      #  break

    # Gewünschten Landkreis laden, falls nicht möglich neue Eingabe einfordern
    while True == True:
        try:
            path_dir = str(f"..\\rki_daten\\Datensatz_vereinzelt\\by_number\\{lk_gesucht}.csv")
            dataset = pd.read_csv(path_dir)
            # continue
        except pd.errors.EmptyDataError:
            print("Der Datensatz für den Landkreis ist nicht vorhanden. Meinten Sie möglicherweise folgenden Landkreis? ")
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
                lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
                if lk_gesucht.isalpha():
                    ges_reih = lk_gesamt.loc[lk_gesamt['column_name'] == "lk_gesucht"]
                    lk_gesucht = ges_reih[0]
                elif lk_gesucht.isdigit():
                    continue
    lk_gesucht.split()
    print(type(lk_gesucht))
    liste_lk=lk_gesucht.append()
    join(lk_gesucht)
    i+=1
print(i)
print(anz_lk)


# aktualitaet.py aufrufen und Aktualität der .csv Datei prüfen
# akt = 0
#if akt <= 1:
 #   zu_akt = lk_gesucht
  #  runpy.run_module(mod_name="aktualitaet", mod_name=f"{zu_akt}")
#else:
 #   break
## sort_meld.py aufrufen und Daten nach Meldedatum sortieren
## sort = 0
#if sort < 1:
#    zu_sort = lk_gesucht
#    runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")
#else:
    #break