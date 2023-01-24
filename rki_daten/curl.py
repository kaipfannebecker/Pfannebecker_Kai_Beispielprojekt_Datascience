import requests
import logging


def main():
    url = 'https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/index.html'
    reqs = requests.get(url)
    whole_download = reqs.text
    with open("output.txt", "w") as text_file:
        print(whole_download, file=text_file)
    logging.info("output.txt wurde aktualisiert.")
