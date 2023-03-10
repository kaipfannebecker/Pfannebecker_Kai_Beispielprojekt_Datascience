import logging

from Methoden.Datengeneration.Data_collection.Helper import curl, delete_done_line, download_url, extract_urls, \
    get_next_url, remove_common, write_to_file_after_five, write_to_file_five_and_lower, xz_extract

# ----------------------------------------------------------------------------------------------------------------------
# Aufgabe des Moduls:
## aufrufen der Module zur Aktualisierung des Datensatzes

# Benötigt:
## Variable "akt"

# Gibt zurück:
## aktualisierten Datensatz

# ----------------------------------------------------------------------------------------------------------------------


def collection(akt):
    if akt == 1:
        curl.main()
        akt = 2
    if akt == 2:
        extract_urls.main()
        akt = 3
    if akt == 3:
        while True:
            finished = remove_common.main()
            if finished == 1:
                break
            if finished == 0:
                next_url = get_next_url.main()
                download_url.main(next_url)
                xz_extract.main()
                x1 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-21-12-00.ndjson.xz"
                x2 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-22-12-00.ndjson.xz"
                x3 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-23-12-00.ndjson.xz"
                x4 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-24-12-00.ndjson.xz"
                x5 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-25-12-00.ndjson.xz"
                list_first_five = [x1, x2, x3, x4, x5]
                s = f"{next_url}"
                count = list_first_five.count(s)

                # if next_url in list_first_five:
                if count > 0:
                    # print("first five")
                    finished_url = write_to_file_five_and_lower.main(next_url)
                else:
                    # print("after five")
                    finished_url = write_to_file_after_five.main(next_url)
                delete_done_line.main(finished_url)


def main(akt):

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler(f"./log/{__name__}.log")
    formatter = logging.Formatter(
        '%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ''function %(funcName)s] %(message)s',
        datefmt='%Y-%m-%d:%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    collection(akt)


# var_akt = 2
# main(var_akt)
