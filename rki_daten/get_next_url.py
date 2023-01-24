import logging


def main():
    urls_unique = open("urls_unique.txt", "r")
    next_url = urls_unique.readline()
    logging.info(f"{next_url} wurde ausgelesen und übergeben.")
    return next_url
