# Hinzufügen von RKI spezifischen Landkreisen
## 11001 Berlin Mitte
## 11002 Berlin Friedrichshain-Kreuzberg
## 11003 Berlin Pankow
## 11004 Berlin Charlottenburg-Wilmersdorf
## 11005 Berlin Spandau
## 11006 Berlin Steglitz-Zehlendorf
## 11007 Berlin Tempelhof-Schöneberg
## 11008 Berlin Neukölln
## 11009 Berlin Treptow-Köpenick
## 11010 Berlin Marzahn-Hellersdorf
## 11011 Berlin Lichtenberg
## 11012 Berlin Reinickendorf

import numpy as np
import pandas as pd

data = np.array([[11001,"Berlin Mitte"], [11002, "Berlin Friedrichshain-Kreuzberg",], [11003, "Berlin Pankow"],
                 [11004, "Berlin Charlottenburg-Wilmersdorf"],[11005,"Berlin Spandau"], [11006, "Berlin Steglitz-Zehlendorf"],
                 [11007, "Berlin Tempelhof-Schöneberg"], [11008,"Berlin Neukölln"], [11009, "Berlin Treptow-Köpenick"],
                 [11010,"Berlin Marzahn-Hellersdorf"], [11011,"Berlin Lichtenberg"], [11012, "Berlin Reinickendorf"]])

#print(data)
#np.savetxt("data.csv", data, delimiter=",")

df_RKI = pd.DataFrame(data)

#print(df_RKI)
df_RKI.to_csv("liste_rki.csv",index=None,columns=None, header=False, encoding='utf-8')
#df_RKI.to_csv("lk_fin.csv", mode='a')
