import logging

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## schreibt die genutzte URL in urls_used.txt

# Benötigt:
## Variable: "finished_url"

# Gibt zurück:
## erweiterte "urls_used.txt"

# ----------------------------------------------------------------------------------------------------------------------


def delete_lin(finished_url):
    with open("./rki_daten/urls_used.txt", "a") as file_object:
        file_object.write(f"{finished_url}")


def main(finished_url):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    delete_lin(finished_url)

    print(f"Die URL {finished_url} wurde vollständig bearbeitet")

    logging.info(f"Die URL {finished_url} wurde vollständig bearbeitet")
