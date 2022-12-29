import runpy
import pandas as pd
from datetime import datetime, timedelta, date
today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')
akt = 0
sort = 0
# NÖTIG: Übergabe von String mit den gewünschten Datensätzen
# in der ersten Spalte nach dem Index als dataframe zu_akt

# sort_meld.py aufrufen und Daten nach Meldedatum sortieren
for sort < 1:
    zu_sort = zu_akt
    runpy.run_module(mod_name="sort_meld", mod_name=f"{zu_sort}")

# Abfrage ob Datensatz aktuell, falls nicht filterung_datensaetze.py aufrufen

for k in zu_akt:
    df = pd.read_csv(rf'C:\Users\Kai\Desktop\Projekt_Datascience\rki_daten\{zu_sort}.csv')
    # prüfe Datum der letzten Zeile in Meldedatum
    last_row = df.iloc[-1]
    if last_row[3] == today:
        continue
    else:
        runpy.run_module(mod_name="filterung_datensaetze")
akt = 1
return akt

quit()


## a.py
# import argparse

# def parse_args():
#    # fmt: off
#    parser = argparse.ArgumentParser()
#    parser.add_argument("--myvar")
#    args = parser.parse_args()
#    # fmt: on
#    return args

# if __name__ == "__main__":
#    args = parse_args()
#    print(args.myvar)

## b.py

# import runpy
# runpy.run_path(path_name='a.py', run_name="__main__")
