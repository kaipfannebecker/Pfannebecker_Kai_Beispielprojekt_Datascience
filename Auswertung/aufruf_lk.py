import pandas as pd
import sys
import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Ruft "anz_lk" Landkreise ab, prüft diese über das Submodul aktualitaet.py auf Aktualität
## und gibt die Liste der Landkreise "liste_lk" zurück

# Benötigt:
## Übergabe von Variable anz_lk; gibt Anzahl der insgesamt gewünschten Landkreise an

# Gibt zurück:
## liste_lk = Liste der Landkreise

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
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------
def main(anz_lk):
    lk_gesamt = einlesen_lk()
    print(lk_gesamt)
    i = 0
    liste_lk = list()
    while i < anz_lk:
        lk_gesucht = eingabe_lk()
        print(lk_gesucht)
        # Falls der Name des Landkreises eingegeben wird, diesen zur zugehörigen Nummer zurordnen
        test_var = check_user_input(lk_gesucht, lk_gesamt)
        print(test_var)
        lk_gesucht = test_var[0]
        reihe_ges = test_var[1]
        print(reihe_ges)
        print(type(reihe_ges))
        lk_laden(lk_gesamt, reihe_ges, lk_gesucht)
        liste_lk = liste_lk.append(lk_gesucht)
        i += 1
    input("Enter")
    print(liste_lk)
    return liste_lk

# ----------------------------------------------------------------------------------------------------------------------
def check_user_input(lk_gesucht, lk_gesamt): # funktioniert noch nicht
    try:
        # Convert it into integer
        lk_gesucht = int(lk_gesucht)
        #reihe_ges = []
        #print("Input is an integer number. Number = ", val)
    except ValueError:
        print(lk_gesamt)
        print(lk_gesucht)
        reihe_ges = lk_gesamt.loc[lk_gesamt['NameLandkreis'] == "lk_gesucht"]
        print(reihe_ges)
        lk_gesucht = reihe_ges['IdLandkreis']
        #return lk_gesucht, reihe_ges
    return lk_gesucht, reihe_ges

# ----------------------------------------------------------------------------------------------------------------------
def einlesen_lk():
    # ließt alle vorhandenen Landkreise ein
    lk_gesamt = pd.read_csv(r'../Liste_der_Landkreise_fuer_Projekt.csv') #C:/Users/Kai/Desktop/Projekt_Datascience
    return lk_gesamt
# ----------------------------------------------------------------------------------------------------------------------
#lk_gesucht=[]

# ----------------------------------------------------------------------------------------------------------------------
def eingabe_lk():
    #lk_gesucht = []
    lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
    #if lk_gesucht.strip().isalpha():
     #   reihe_ges = lk_gesamt.loc[lk_gesamt['Name_Landkreis'] == "lk_gesucht"]
      #  lk_gesucht = reihe_ges['Id_Landkreis']
        #print(lk_gesucht)
    #elif lk_gesucht.isdigit():
     #   break
    return lk_gesucht

# ----------------------------------------------------------------------------------------------------------------------
# noch nötig?
    #if lk_gesucht.strip().isalpha():
     #   reihe_ges = lk_gesamt.loc[lk_gesamt['Name_Landkreis'] == "lk_gesucht"]
      #  lk_gesucht = reihe_ges['Id_Landkreis']
      #  print(lk_gesucht)
    #elif lk_gesucht.isdigit():
     #   break

    #print(lk_gesucht)
    #print(type(lk_gesucht))

# ----------------------------------------------------------------------------------------------------------------------
def lk_laden(lk_gesamt, reihe_ges, lk_gesucht):
    # Gewünschten Landkreis laden, falls nicht möglich neue Eingabe einfordern
    while True == True:
        try:
            print(lk_gesucht)
            print(type(lk_gesucht))
            path_dir = str(fr"..\rki_daten\Datensatz_vereinzelt\by_number\{lk_gesucht[0]}.csv")
            dataset = pd.read_csv(path_dir) # Zeile nötig?
            break
        except FileNotFoundError or OSError:  # pd.errors.EmptyDataError:
            print("Der Datensatz für den Landkreis ist nicht vorhanden.")
            if len(reihe_ges):
                namen_lk = lk_gesamt['1']
            else:
                namen_lk = "leer"
            #alt_lk = k for k in lk_gesamt if f'{lk_gesucht}' in k
            if len(reihe_ges):
                alt_lk = namen_lk.loc[namen_lk['1'] == reihe_ges['1']]
            else:
                alt_lk = "leer"
            print(f"Meinten Sie möglicherweise folgenden Landkreis: {alt_lk}?")
            weiter = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:\n" 
                            "1. Erneute Eingabe eines Landkreises\n" 
                            "2. Programm beenden\n"
                           "" )
            if weiter == "2":
                sys.exit()
            else:
                lk_gesucht = eingabe_lk()
                test_var = check_user_input(lk_gesucht, lk_gesamt)
                lk_gesucht = test_var[0]
                reihe_ges = test_var[1]




               # lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
               # if lk_gesucht.isalpha():
                #    ges_reih = lk_gesamt.loc[lk_gesamt['1'] == "lk_gesucht"]
                #    lk_gesucht = ges_reih[0]
                # elif lk_gesucht.isdigit():
                    # continue
    #lk_gesucht.split()
    #print(type(lk_gesucht))
    #
    #join(lk_gesucht)
