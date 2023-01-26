import gc
import pandas as pd
import json
import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
##

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------


def write_to_file_first(data):

    with open('./rki_daten/next_dataset.ndjson', mode='r', encoding='utf-8') as myfile:
        for line in myfile:
            inline = json.loads(line)
            data.append(inline)
    df = pd.DataFrame(data)
    # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
    if 'NeuerFall' not in df:
        df['NeuerFall'] = 1
    if "RefdatumISO" not in df:
        df["RefdatumISO"] = 1
    if "Refdatum" not in df:
        df["Refdatum"] = 1
    #
    df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"])  # "DatenstandISO",
    df.to_csv("./rki_daten/Datensatz_Neuinfektionen_gesamt.csv")
    del df
    gc.collect()


def main(next_url):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    data = []
    write_to_file_first(data)
    logging.info(f"{next_url}_fertig")
    finished_url = next_url
    return finished_url
