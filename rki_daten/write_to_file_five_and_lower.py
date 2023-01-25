import gc
import pandas as pd
import json
import logging


def main(next_url):
    data = []
    with open('next_dataset.ndjson', mode='r', encoding='utf-8') as myfile:
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
    df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
    del df
    gc.collect()
    logging.info(f"{next_url}_fertig")
    finished_url = next_url
    return finished_url
