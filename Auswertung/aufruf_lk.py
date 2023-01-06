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
anz_lk=3

# ----------------------------------------------------------------------------------------------------------------------
def check_user_input(input):
    try:
        # Convert it into integer
        lk_gesucht = int(input)
        #print("Input is an integer number. Number = ", val)
    except ValueError:
        reihe_ges = lk_gesamt.loc[lk_gesamt['Name_Landkreis'] == "lk_gesucht"]
        print(reihe_ges)
        lk_gesucht = reihe_ges['Id_Landkreis']

# ----------------------------------------------------------------------------------------------------------------------
# ließt alle vorhandenen Landkreise ein
lk_gesamt = pd.read_csv(r'../Liste_der_Landkreise_fuer_Projekt.csv') #C:/Users/Kai/Desktop/Projekt_Datascience

i = 0
lk_gesucht=[]

while i < anz_lk:
    print(i)
    print(anz_lk)
    # fragt den gesuchten Landkreis ab.
    lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
    print(lk_gesucht)
    print(type(lk_gesucht))

#    https: // pynative.com / python - check - user - input - is -number - or -string /

    # Falls der Name des Landkreises eingegeben wird, diesen zur zugehörigen Nummer zurordnen
    check_user_input(lk_gesucht)
    print(lk_gesucht)
    print(type(lk_gesucht))
    #if lk_gesucht.strip().isalpha():
    #    reihe_ges = lk_gesamt.loc[lk_gesamt['Name_Landkreis'] == "lk_gesucht"]
    #    lk_gesucht = reihe_ges['Id_Landkreis']
    #    print(lk_gesucht)
    #elif lk_gesucht.isdigit():
      #  break

    # Gewünschten Landkreis laden, falls nicht möglich neue Eingabe einfordern
    while True == True:
        try:
            path_dir = str(f"..\\rki_daten\\Datensatz_vereinzelt\\by_number\\{lk_gesucht}.csv")
            dataset = pd.read_csv(path_dir)
            break
        except FileNotFoundError:  # pd.errors.EmptyDataError:
            print("Der Datensatz für den Landkreis ist nicht vorhanden.")
            namen_lk = lk_gesamt['1']
            print(namen_lk)
            print(lk_gesamt)
            print(lk_gesamt["0"])
            #alt_lk = k for k in lk_gesamt if f'{lk_gesucht}' in k
            alt_lk = namen_lk.loc[namen_lk['1'] == reihe_ges['1']]

            #df.loc[lambda df: df['shield'] == 8]
            #df.y.str.contains('D')
            #df = df.loc[df['y'] == D]
                #contains('D', case=True))
            #print(df[df.y.str.contains('D')])

            #alt_lk = namen_lk.loc[namen_lk[1].isin(f'{lk_gesucht}')]
            #alt_lk = {k for k in namen_lk if f'{lk_gesucht}' in k}
            print(alt_lk)
            print(f"Meinten Sie möglicherweise folgenden Landkreis: {alt_lk}?")
            weiter = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:" 
                            "1. erneute Eingabe eines Landkreises" 
                            "2. Programm beenden" )
            if weiter == 2:
                quit()
            else:
                lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
                if lk_gesucht.isalpha():
                    ges_reih = lk_gesamt.loc[lk_gesamt['1'] == "lk_gesucht"]
                    lk_gesucht = ges_reih[0]
                # elif lk_gesucht.isdigit():
                    # continue
    #lk_gesucht.split()
    #print(type(lk_gesucht))
    #liste_lk=lk_gesucht.append()
    #join(lk_gesucht)
    i+=1
print(i)
print(anz_lk)



