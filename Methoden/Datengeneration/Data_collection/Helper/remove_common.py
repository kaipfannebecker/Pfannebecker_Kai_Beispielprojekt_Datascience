import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## vergleicht die beiden Listen "urls_used.txt" und "urls_total.txt". Gibt die Differenz als "urls_unique.txt".
## Bei Gleichheit beider Listen Finished = 1

# Benötigt:
## Datei: "urls_used.txt", "urls_total.txt"

# Gibt zurück:
## Variable Finished (0, solange noch URLs zu bearbeiten sind\ 1, wenn beide Listen identisch sind)
## Datei: "urls_unique.txt"

# ----------------------------------------------------------------------------------------------------------------------


def remove_common(urls_total, urls_done):
    urls_total = urls_total.split("\n")
    urls_done = urls_done.split("\n")
    for i in urls_total[:]:
        if i in urls_done:
            urls_total.remove(i)
            # b.remove(i)
    return urls_total


def main():

    urls_done_txt = open("./rki_daten/urls_used.txt", "r")
    urls_done = urls_done_txt.read()
    urls_total_txt = open("./rki_daten/urls_total.txt", "r")
    urls_total = urls_total_txt.read()

    urls_to_do = remove_common(urls_total, urls_done)
    if not urls_to_do:
        finished = 1
    else:
        with open('./rki_daten/urls_unique.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(urls_to_do))
            finished = 0

    logging.info(f"urls_unique.txt wurde aktualisiert. Es wurde der Wert finished = {finished} zurück gegeben")
    return finished
