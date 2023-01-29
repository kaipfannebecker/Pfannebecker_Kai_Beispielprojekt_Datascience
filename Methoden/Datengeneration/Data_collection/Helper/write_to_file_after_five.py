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


def write_file_after_five(data):
    #with open('./rki_daten/next_dataset.ndjson', mode='r', encoding='utf-8') as myfile:
    with open(r'./rki_daten/next_dataset.ndjson', mode='r', encoding='utf-8') as myfile:

        for line in myfile:
            inline = json.loads(line)
            if inline["NeuerFall"] == 1 or inline["NeuerFall"] == -1:
                data.append(inline)
    df = pd.DataFrame(data)
    if 'NeuerFall' not in df:
        df['NeuerFall'] = 1
    if "RefdatumISO" not in df:
        df["RefdatumISO"] = 1
    if "Refdatum" not in df:
        df["Refdatum"] = 1
    if "ObjectId" not in df:
        df["ObjectId"] = 1
    df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"])  # "DatenstandISO",
    df.to_csv(r"./rki_daten/Datensatz_Neuinfektionen_gesamt.csv", mode="a")
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
    write_file_after_five(data)
    logging.info(f"{next_url}_fertig")
    finished_url = next_url
    return finished_url

