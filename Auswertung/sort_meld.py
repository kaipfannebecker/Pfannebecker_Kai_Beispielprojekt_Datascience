import pandas as pd
import os

directory = os.fsencode("C:\Users\Kai\Desktop\Projekt_Datascience\Auswertung")

# Iteriere über alle Files in einem Ordner
if zu_sort == True and len(zu_sort) == 1:
    for file in os.listdir(directory):
    filename = zu_sort.csv
    dataframe = pd.read_csv(filename)
    dataframe.sort_values(by=[3])
    dataframe.to_csv(f"{filename}.csv")
else:
    for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # suche nach .csv Dateien
        if filename.endswith(".csv"):
            dataframe = pd.read_csv(filename)
            dataframe.sort_values(by=[3])
            dataframe.to_csv(f"{filename}.csv")
sort = 1
return sort
quit()
