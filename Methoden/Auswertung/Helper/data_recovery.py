import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## sortiert die eingegebenen Daten nach geünschter Varaible = 1 sowie = -1, rechnet die entsprechende Anzahl um
## und addiert diese

# Benötigt:
## Variablen: "var_da_sort", "var_da_anz", "data_single_lk_neu"

# Gibt zurück:
## Variable: "data_neu_ges"

# ----------------------------------------------------------------------------------------------------------------------
################################################ Definierte Funktionen #################################################
# ----------------------------------------------------------------------------------------------------------------------


def main(var_da_sort, var_da_anz, data_single_lk_neu):
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter('%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in '
                                  'function %(funcName)s] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    data_neu_ges = data_recovery(var_da_sort, var_da_anz, data_single_lk_neu)
    return data_neu_ges


def data_recovery(var_da_sort, var_da_anz, data_single_lk_neu):
    data_neu_pos_1 = data_single_lk_neu.loc[data_single_lk_neu[f'{var_da_sort}'] == 1.0]
    data_neu_pos = data_neu_pos_1.sum()
    data_neu_pos_num = data_neu_pos[f"{var_da_anz}"]
    data_neu_neg_1 = data_single_lk_neu.loc[data_single_lk_neu[f"{var_da_sort}"] == -1.0]
    if data_neu_neg_1.empty:
        data_neu_neg_num = 0
    else:
        data_neu_neg = data_neu_neg_1.sum()
        data_neu_neg_num = data_neu_neg[f"{var_da_anz}"]
    data_neu_ges = data_neu_pos_num + data_neu_neg_num
    return data_neu_ges

# ----------------------------------------------------------------------------------------------------------------------
#################################################### Programmstart #####################################################
# ----------------------------------------------------------------------------------------------------------------------

# main()
