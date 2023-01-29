import pandas as pd
import numpy as np

import sys
import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## Ruft "anz_lk" Landkreise_Bundeslaender ab, prüft diese über das Submodul aktualitaet.py auf Aktualität
## und gibt die Liste der Landkreise_Bundeslaender "liste_lk" zurück

# Benötigt:
## Übergabe von Variable anz_lk; gibt Anzahl der insgesamt gewünschten Landkreise_Bundeslaender an

# Gibt zurück:
## liste_lk = Liste der Landkreise_Bundeslaender
## Ausgabe in geschweiften Klammern; im aufrufenden Programm danach folgende Zeile nötig:
### liste_lk = aufruf_lk.main(anz_lk)
### liste_lk = str(liste_lk).replace('[', '').replace(']', '')

# ----------------------------------------------------------------------------------------------------------------------
################################################ Definierte Funktionen #################################################
# ----------------------------------------------------------------------------------------------------------------------


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    lk_gesamt = einlesen_lk()
    logger.info(f'Tabelle mit allen Landkreisen erfolgreich eingelesen.')
    liste_lk = []
    lk_gesucht = eingabe_lk()
    lk_gesucht = check_user_input(lk_gesucht, lk_gesamt)
    liste_lk = lk_laden(lk_gesamt, lk_gesucht)
    liste_lk_1 = np.int64(liste_lk)
    reihe_lk = lk_gesamt.loc[lk_gesamt['IdLandkreis'] == liste_lk_1]
    name_lk = reihe_lk["NameLandkreis"].values[0]
    logger.info(f"Das Subprogramm aufruf_lk ist erfolgreich durchgelaufen und gibt {liste_lk} zurück.")
    return liste_lk, name_lk

# ----------------------------------------------------------------------------------------------------------------------


def check_user_input(lk_gesucht, lk_gesamt):
    print(lk_gesucht)
    try:
        # Convert it into integer
        lk_gesucht = int(lk_gesucht)
    except ValueError:
        reihe_ges = lk_gesamt.loc[lk_gesamt['NameLandkreis'] == f"{lk_gesucht}"]
        if reihe_ges.empty:  # testet ob reihe_ges leer ist. Falls nein, wird lk_gesucht ersetzt.
            return lk_gesucht
        else:
            lk_gesucht = reihe_ges['IdLandkreis']
    return lk_gesucht

# ----------------------------------------------------------------------------------------------------------------------


def einlesen_lk():
    # liest alle vorhandenen Landkreise_Bundeslaender ein
    lk_gesamt = pd.read_csv(r'./Liste_der_Landkreise_fuer_Projekt.csv')  # C:/Users/Kai/Desktop/Projekt_Datascience
    return lk_gesamt

# ----------------------------------------------------------------------------------------------------------------------


def eingabe_lk():
    lk_gesucht = input("Bitte den Namen des gewünschten Landkreises eingeben ")
    return lk_gesucht

# ----------------------------------------------------------------------------------------------------------------------


def lk_laden(lk_gesamt, lk_gesucht):
    # Gewünschten Landkreis laden, falls nicht möglich neue Eingabe einfordern
    while True:
        try:
            if isinstance(lk_gesucht, int):
                val_lk_ges = str(lk_gesucht).replace("'", "")
            else:
                val_lk_ges = lk_gesucht.iloc[0]
            path_dir = str(fr".\rki_daten\Datensatz_vereinzelt\by_number\{val_lk_ges}.csv")
            open(path_dir)
            print("Der Datensatz für den Landkreis ist vorhanden.")
            break
        except (FileNotFoundError, AttributeError):  # pd.errors.EmptyDataError: #OSError,
            print("Der Datensatz für den Landkreis ist nicht vorhanden.")
            try:
                # Convert it into integer
                val_lk_ges = int(val_lk_ges)
            except ValueError:
                val_lk_ges = val_lk_ges
            if isinstance(val_lk_ges, str):
                namen_lk = lk_gesamt['NameLandkreis']
                alt_lk = namen_lk[namen_lk.str.contains(f"{lk_gesucht}")]
                print(f"Meinten Sie möglicherweise folgenden Landkreis: {alt_lk.iloc[0]}?")
            if isinstance(val_lk_ges, int):
                id_lk = lk_gesamt['IdLandkreis']
                id_lk = id_lk.sort_values()
                alt_lk_1 = id_lk.iloc[np.searchsorted(id_lk.values, [val_lk_ges])]
                alt_lk_2 = id_lk.iloc[(np.searchsorted(id_lk.values, [val_lk_ges]) - 1)]
                print(f"Meinten Sie möglicherweise folgenden Landkreis: {alt_lk_2.iloc[0]} oder {alt_lk_1.iloc[0]}?")
            weiter = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:\n" 
                            "1. Erneute Eingabe eines Landkreises\n" 
                            "2. Alle verfügbaren Landkreise_Bundeslaender anzeigen\n"
                            "3. Programm beenden\n"
                           "" )
            if weiter == "2":
                pd.set_option('display.max_rows', None)
                print(lk_gesamt['NameLandkreis'])
                weiter1 = input("Was möchten Sie tun? Drücken Sie bitte 1 oder 2:\n"
                               "1. Erneute Eingabe eines Landkreises\n"
                               "2. Programm beenden\n"
                               "")
                if weiter1 == "2":
                    sys.exit()
                if weiter1 == "1":
                    lk_gesucht = eingabe_lk()
                    lk_gesucht = check_user_input(lk_gesucht, lk_gesamt)
            if weiter == "3":
                sys.exit()
            if weiter == "1":
                lk_gesucht = eingabe_lk()
                lk_gesucht = check_user_input(lk_gesucht, lk_gesamt)
    return val_lk_ges

# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------

# main()
