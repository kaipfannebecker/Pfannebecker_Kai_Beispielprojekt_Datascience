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

data = np.array([[11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012],
         ["Berlin Mitte", "Berlin Friedrichshain-Kreuzberg", "Berlin Pankow", "Berlin Charlottenburg-Wilmersdorf",
         "Berlin Spandau", "Berlin Steglitz-Zehlendorf", "Berlin Tempelhof-Schöneberg", "Berlin Neukölln",
         "Berlin Treptow-Köpenick", "Berlin Marzahn-Hellersdorf", "Berlin Lichtenberg", "Berlin Reinickendorf"]])

#print(data)
#np.savetxt("data.csv", data, delimiter=",")

df_RKI = pd.DataFrame(data)

#print(df_RKI)
df_RKI.to_csv("df_RKI.csv",index=None,columns=None, header=False)
#df_RKI.to_csv("lk_fin.csv", mode='a')