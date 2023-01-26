import lzma
import logging
# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
##

# Benötigt:
##

# Gibt zurück:
##

# ----------------------------------------------------------------------------------------------------------------------

def open_xz():
    with lzma.open("./rki_daten/date.xz", mode='rt', encoding='utf-8') as fin:
        file_content = fin.read().split('\n')
        # Problem: Letzte Zeile ist leer. Diese muss gelöscht werden, damit json.loads keinen Fehler erzeugt.
        file_content = file_content[:-1]
        with open('./rki_daten/next_dataset.ndjson', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(file_content))


def main():

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    open_xz()
    logging.info(f"Die Datei next_dataset.ndjson wurde erfolgreich aktualisiert.")
