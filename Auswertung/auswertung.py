from os import path
import pandas as pd
import os
from datetime import datetime, timedelta, date
today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')

directory = os.fsencode("C:\Users\Kai\Desktop\Projekt_Datascience\Auswertung")

# Iteriere über alle Files in einem Ordner
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # suche nach .csv Dateien
    if filename.endswith(".csv"):
        dataframe = pd.read_csv(filename)
        dataframe.sort_values(by=[3])
        
