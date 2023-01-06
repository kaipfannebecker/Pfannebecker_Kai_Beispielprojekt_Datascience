import json
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## NDJSON Datei lesen und als csv Datei ausgeben

# Benötigt:

# Gibt zurück:

# ----------------------------------------------------------------------------------------------------------------------
#json_in=json.loads(json_in)

#json_in = pd.read_json("data_2020-12-01-03-33.ndjson", lines=True)
#json_in.to_csv("data_2020-12-01-03-33.csv")

json_in = pd.read_json("data_2020-03-21-12-00.ndjson", lines=True)
json_in.to_csv("data_2020-03-21-12-00.csv")