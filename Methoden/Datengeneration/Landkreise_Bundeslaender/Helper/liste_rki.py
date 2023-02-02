import numpy as np
import pandas as pd

import logging

# ----------------------------------------------------------------------------------------------------------------------

# Aufgabe des Moduls:
## Hinzufügen von RKI spezifischen Landkreisen
### 11001 Berlin-Mitte
### 11002 Berlin-Friedrichshain-Kreuzberg
### 11003 Berlin-Pankow
### 11004 Berlin-Charlottenburg-Wilmersdorf
### 11005 Berlin-Spandau
### 11006 Berlin-Steglitz-Zehlendorf
### 11007 Berlin-Tempelhof-Schöneberg
### 11008 Berlin-Neukölln
### 11009 Berlin-Treptow-Köpenick
### 11010 Berlin-Marzahn-Hellersdorf
### 11011 Berlin-Lichtenberg
### 11012 Berlin-Reinickendorf

# Benötigt:
## -

# Gibt zurück:
## Datei "liste_rki.csv"

# ----------------------------------------------------------------------------------------------------------------------



def rki_dataset():
    data = np.array([[11001, "Berlin Mitte", 11], [11002, "Berlin Friedrichshain-Kreuzberg", 11],
                     [11003, "Berlin Pankow", 11], [11004, "Berlin Charlottenburg-Wilmersdorf", 11],
                     [11005, "Berlin Spandau", 11], [11006, "Berlin Steglitz-Zehlendorf", 11],
                     [11007, "Berlin Tempelhof-Schöneberg", 11], [11008, "Berlin Neukölln", 11],
                     [11009, "Berlin Treptow-Köpenick", 11], [11010, "Berlin Marzahn-Hellersdorf", 11],
                    [11011, "Berlin Lichtenberg", 11], [11012, "Berlin Reinickendorf", 11]]
                    )

    df_RKI = pd.DataFrame(data)
    df_RKI[0].astype(str)
    df_RKI.to_csv("liste_rki.csv", index=None, columns=None, header=False, encoding='utf-8')

def main():
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
                                  'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    rki_dataset()