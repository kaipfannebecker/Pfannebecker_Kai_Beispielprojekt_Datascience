from bs4 import BeautifulSoup
import logging


def main():
    # url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
    reqs = open("output.txt")

    soup = BeautifulSoup(reqs, 'html.parser')

    with open(r'C:\Users\Kai\Documents\GitHub\Projekt_Datascience\rki_daten\urls_total.txt', 'w') as fp:
        for link in soup.find_all('a'):
            spe_url = link.get('href')
            fp.write("%s\n" % spe_url)
    logging.info("urls_total.txt wurde aktualisiert.")
