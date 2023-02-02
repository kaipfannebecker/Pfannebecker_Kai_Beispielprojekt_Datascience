import pandas as pd

import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## liest den Gesamtdatensatz ein und splittet diesen in verschiedene Subdatensätze, getrennt nach Landkreis
## und/oder Bundesland

# Benötigt:
## "Datensatz_Neuinfektionen_gesamt.csv", "Liste_der_Landkreise_fuer_Projekt_1.csv"

# Gibt zurück:
## vereinzelte Listen in den entsprechenden Ordnern

# ----------------------------------------------------------------------------------------------------------------------

def filterung():
    ## aktuellen Datensatz des RKI importieren
    dataset_rki = pd.read_csv('./Datensatz_Neuinfektionen_gesamt.csv', on_bad_lines="warn")

    # dataset_rki = pd.read_csv('.\\Datensatz_gesamt\\2021-04-02_Deutschland_SarsCov2_Infektionen.csv')
    tab_lk = pd.read_csv('./Liste_der_Landkreise_fuer_Projekt_1.csv')

    # groupby the desired column and iterate through the groupby object
    for Id_lk, dataset_rki in dataset_rki.groupby('IdLandkreis'):
        row_lk = tab_lk.loc[tab_lk["IdLandkreis"] == Id_lk]
        #if Id_lk != -1:
        #   name_lk = row_lk['NameLandkreis']
        #   print(name_lk)
        #   print(type(name_lk))
        #   name_lk_2 = name_lk.iat[0]
            # print(name_lk_2)
            # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk_2}.csv', index=False, mode='w')
        ## save the dataframe for each group to a csv; seperated for each Landkreis
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\Landkreis\\{number_lk}.csv', index=False, mode='a')  # welcher funkioniert?
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk_2}.csv', index=False, mode='a')  # welcher funkioniert?
        dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\Landkreis\\{Id_lk}.csv', index=False, mode='w')
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\Landkreis\\{number_lk}_{name_lk}.csv', index=False, mode='a')

    for Id_bl, dataset_rki in dataset_rki.groupby('IdBundesland'):
        row_bl = tab_lk.loc[tab_lk["IdBundesland"] == Id_bl]
        # if Id_bl != -1:
        #    name_bl = row_lk['NameLandkreis']
        #   name_bl_2 = name_bl.iat[0]
            # print(name_lk_2)
            # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_name\\{name_lk_2}.csv', index=False, mode='w')
        ## save the dataframe for each group to a csv; seperated for each Landkreis
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\Bundesland\\by_name\\{name_bl_2}.csv', index=False, mode='a')
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\Bundesland\\by_name\\{name_bl_2}.csv', index=False, mode='a')
        dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number\\Bundesland\\{Id_bl}.csv', index=False, mode='w')
        # dataset_rki.to_csv(f'.\\Datensatz_vereinzelt\\by_number_name\\Bundesland\\{Id_bl}_{name_bl}.csv', index=False, mode='a')


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    filterung()
    logging.info("Die Datensätze wurden gefiltert")
