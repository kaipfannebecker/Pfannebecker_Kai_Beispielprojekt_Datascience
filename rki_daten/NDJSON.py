import json
import pandas as pd
import os
# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## NDJSON Datei lesen und als csv Datei ausgeben

# Benötigt:

# Gibt zurück:

# ----------------------------------------------------------------------------------------------------------------------
#json_in=json.loads(json_in)

#json_in = pd.read_json("data_2020-12-01-03-33.ndjson", lines=True)
#json_in.to_csv("data_2020-12-01-03-33.csv")

#directory = os.fsencode(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten')

#for file in os.listdir(directory):
#    filename = os.fsdecode(file)
# suche nach .csv Dateien
#    if filename.endswith(".csv"):
#        json_in = pd.read_json(f"data_2020-12-01-03-33.ndjson", lines=True)
#        json_in.to_csv(f"data_2020-12-01-03-33.csv")

json_in = pd.read_json("data_2020-12-01-03-33.ndjson", lines=True)
#print(json_in)
json_in.to_csv("data_2020-04-26-04-06.csv")