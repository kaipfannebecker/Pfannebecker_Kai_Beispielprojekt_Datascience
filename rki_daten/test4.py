import requests
from bs4 import BeautifulSoup

# nötig: log generieren und in abschnitten einlesen

url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')


for link in soup.find_all('a'):
    spe_url = link.get('href')
    with open("urls_used.txt", "a") as urls_used:
        urls_used.write(f"{spe_url}\n")
        urls_used.close()