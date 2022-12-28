# import os.path
from os import path
import os
from datetime import datetime, timedelta, date
today = date.today()
yesterday = datetime.now() - timedelta(1)
datetime.strftime(yesterday, '%Y-%m-%d')






directory = os.fsencode(directory_in_str)

# Abfrage nach gewünschtem Datum
gewdatum = input("Bitte das gewünschte Datum im Format YYYY-MM-DD eingeben.")

# Erstelle die kombinierte Tabelle, falls diese nicht existiert
combined_exists = path.exists(f"combined_lk_table_{gewdatum}.csv")
if combined_exists:
    continue
else:
    combined_lk_table = []


# Iteriere über alle Files in einem Ordner
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # suche nach .csv Dateien
    if filename.endswith(".csv"):
        # print(os.path.join(directory, filename))
        tempTuple = os.path.splitext(filename)
        # print("The tuple is:", tempTuple)
        lknr = tempTuple[0]
        # Prüfe wie aktuell Daten sind und aktualisiere gegebenenfalls auf heute
        if date is today:
            continue
        else:
            for date in
                # füge zeilen bis zu heute hinzu

        # füge die Werte des gewünschten Tages zur gesamten Tabelle hinzu
        corval = file["Datum" == gewdatum]
        ## A series object with same index as dataframe
        # series_obj = pd.Series(['Raju', 21, 'Bangalore', 'India'],
        #                       index=dfObj.columns)
        ## Add a series as a row to the dataframe
        # mod_df = dfObj.append(series_obj,
        #                      ignore_index=True)
        combined_lk_table = combined_lk_table.append(corval, ignore_index=True)
        continue
    else:
        continue

combined_lk_table.to_csv(f"combined_lk_table_{gewdatum}.csv", mode ="a")

