import logging
import urllib.request


def main(next_url):
    urllib.request.urlretrieve(next_url, "date.xz")
    logging.info(f"Die URL {next_url} wurde erfolgreich herunter geladen.")
    return next_url
