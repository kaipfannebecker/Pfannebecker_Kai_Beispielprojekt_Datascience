import requests
from bs4 import BeautifulSoup
import lzma
import urllib.request
import pandas as pd
import json

url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
data = []
urls = []
i=1
data_neuinf_ges = []
data_neuinf_ges = pd.DataFrame(data_neuinf_ges)
# data = pd.DataFrame(data)

for link in soup.find_all('a'):
    spe_url = link.get('href')
    ## Linkliste erzeugen und URL in Variable übergeben funktioniert
    urllib.request.urlretrieve(spe_url, "date.xz")
    with lzma.open("date.xz", mode='rt') as fin:
        file_content = fin.read().split('\n')
    for line in file_content:
        data.append(json.loads(line))
        df = pd.DataFrame(data)
        break
        # Die ersten 4 Tage hatten eine andere Notation; deshalb müssen hierfür extra Spalten angelegt werden.
    if 'NeuerFall' not in df:
        df['NeuerFall']= 1
    if "RefdatumISO" not in df:
        df["RefdatumISO"]= 1
    if "Refdatum" not in df:
        df["Refdatum"] = 1
        #
    df = df.drop(columns=["RefdatumISO", "Refdatum", "Datenstand", "ObjectId", "Meldedatum"]) #"DatenstandISO",
    nur_neu = df.loc[df["NeuerFall"] == 1]
    nur_corr = df.loc[df["NeuerFall"] == -1]
    neue_daten = [data_neuinf_ges, nur_neu, nur_corr]
    data_neuinf_ges = pd.concat(neue_daten)
    data_neuinf_ges.to_csv(f"Datensatz_Neuinfektionen_gesamt.csv")
    #data_neuinf_ges_2.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
    print(f"{fin}_fertig")
    continue

# df = pd.DataFrame(data)
#df.to_csv("Datensatz_Neuinfektionen_gesamt.csv")
