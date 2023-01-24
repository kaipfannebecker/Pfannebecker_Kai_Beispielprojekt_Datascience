import lzma
import logging


def main():
    with lzma.open("date.xz", mode='rt', encoding='utf-8') as fin:
        file_content = fin.read().split('\n')
        # Problem: Letzte Zeile ist leer. Diese muss gelöscht werden, damit json.loads keinen Fehler erzeugt.
        file_content = file_content[:-1]
        print(type(file_content))
        with open('next_dataset.ndjson', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(file_content))

    logging.info(f"Die Datei next_dataset.ndjson wurde erfolgreich aktualisiert.")
