import requests
import gc
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer as strainer
import lzma
import urllib.request
import pandas as pd
import json
import os
from datetime import datetime

# nötig: log generieren und in abschnitten einlesen

url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
#only_item_cells = strainer("div", attrs={"class": "item-cell"})
#page_soup = soup(page_html, 'html.parser', parse_only=only_item_cells)

data = []
urls = []
i = 1
j = 1
data_neuinf_ges = []
data_neuinf_ges = pd.DataFrame(data_neuinf_ges)
# data = pd.DataFrame(data)

for link in soup.find_all('a'):
    spe_url = link.get('href')
    link.decompose()
    with open("urls_used.txt") as urls_used:
        if spe_url in urls_used.read():
            urls_used.close
            # print("uebersprungen")
            continue
        else:
            urls_used.close
            ## Linkliste erzeugen und URL in Variable übergeben funktioniert
            urllib.request.urlretrieve(spe_url, "date.xz")
            #print(datetime.now().strftime("%H:%M:%S.%f"))
            with lzma.open("date.xz", mode='rt', encoding='utf-8') as fin:
                file_content = fin.read().split('\n')
                # Problem: Letzte Zeile ist leer. Diese muss gelöscht werden, damit json.loads keinen Fehler erzeugt.
                file_content = file_content[:-1]
                #print(datetime.now().strftime("%H:%M:%S.%f"))
            if j<5:
                for line in file_content:
                    # data.append(json.loads(line))
                    inline = json.loads(line)
                    data.append(inline)
                df = pd.DataFrame(data)
                # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
                #if 'NeuerFall' not in df:
                #    df['NeuerFall'] = 1
                if "RefdatumISO" not in df:
                    df["RefdatumISO"] = 1
                if "Refdatum" not in df:
                    df["Refdatum"] = 1
                #
                df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"])  # "DatenstandISO",
                nur_neu = df.loc[df["NeuerFall"] == 1]
                nur_corr = df.loc[df["NeuerFall"] == -1]
                neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
                data_neuinf_ges = pd.concat(neue_daten)
                data_neuinf_ges.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
                # df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
                #output_path = "Datensatz_Neuinfektionen_gesamt.csv"
                #df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
                del df
                gc.collect()
                print(f"{spe_url}_fertig")
                j = j+1
                print(j)
                with open("urls_used.txt", "a+") as file_object:
                    # Move read cursor to the start of file.
                    file_object.seek(0)
                    # If file is not empty then append '\n'
                    check_log = file_object.read(100)
                    if len(check_log) > 0:
                        file_object.write("\n")
                    # Append text at the end of file
                    file_object.write(f"{spe_url}")
                    urls_used.close
                continue
            else:
                for line in file_content:
                    # data.append(json.loads(line))
                    inline = json.loads(line)
                    #print(inline)
                    #print(datetime.now().strftime("%H:%M:%S.%f"))
                    if inline["NeuerFall"] == 1 or inline["NeuerFall"] == -1:
                        data.append(inline)
                    #print(datetime.now().strftime("%H:%M:%S.%f"))
                df = pd.DataFrame(data)
                #print(datetime.now().strftime("%H:%M:%S.%f"))
    #               print("hallowelt")
                    # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
                if 'NeuerFall' not in df:
                    df['NeuerFall'] = 1
                if "RefdatumISO" not in df:
                    df["RefdatumISO"] = 1
                if "Refdatum" not in df:
                    df["Refdatum"] = 1
                #
                df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"]) #"DatenstandISO",
            #nur_neu = df.loc[df["NeuerFall"] == 1]
            #nur_corr = df.loc[df["NeuerFall"] == -1]
            #neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
            #data_neuinf_ges = pd.concat(neue_daten)
            #data_neuinf_ges.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
                df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
                #output_path = "Datensatz_Neuinfektionen_gesamt.csv"
                #df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
                del df
                gc.collect()
                print(f"{spe_url}_fertig")
                with open("urls_used.txt", "a+") as file_object:
                    # Move read cursor to the start of file.
                    file_object.seek(0)
                    # If file is not empty then append '\n'
                    check_log = file_object.read(100)
                    if len(check_log) > 0:
                        file_object.write("\n")
                    # Append text at the end of file
                    file_object.write(f"{spe_url}")
                    urls_used.close
            continue

# df = pd.DataFrame(data)
#df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
