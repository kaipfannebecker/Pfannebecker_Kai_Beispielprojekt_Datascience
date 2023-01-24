import logging


def main(finished_url):
    with open("urls_used.txt", "a") as file_object:
        file_object.write(f"{finished_url}")
    logging.info(f"Die URL {finished_url} wurde vollständig bearbeitet")
