import logging


def remove_common(urls_total, urls_done):
    urls_total = urls_total.split("\n")
    urls_done = urls_done.split("\n")
    for i in urls_total[:]:
        if i in urls_done:
            urls_total.remove(i)
            # b.remove(i)
    return urls_total


def main():

    urls_done_txt = open("urls_used.txt", "r")
    urls_done = urls_done_txt.read()
    urls_total_txt = open("urls_total.txt", "r")
    urls_total = urls_total_txt.read()

    urls_to_do = remove_common(urls_total, urls_done)
    if not urls_to_do:
        finished = 1
    else:
        with open('urls_unique.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(urls_to_do))
            finished = 0

    logging.info(f"urls_unique.txt wurde aktualisiert. Es wurde der Wert finished = {finished} zurück gegeben")
    return finished


