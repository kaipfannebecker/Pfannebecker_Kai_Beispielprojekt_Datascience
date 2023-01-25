import remove_common
import get_next_url
import extract_urls
import download_url
import xz_extract
import delete_done_line
import write_to_file_after_five
import write_to_file_five_and_lower
import curl


def main():
    curl.main()
    extract_urls.main()
    while True:
        finished = remove_common.main()
        if finished == 1:
            break
        if finished == 0:
            next_url = get_next_url.main()
            next_url = download_url.main(next_url)
            xz_extract.main()
            x1 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-21-12-00.ndjson.xz"
            x2 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-22-12-00.ndjson.xz"
            x3 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-23-12-00.ndjson.xz"
            x4 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-24-12-00.ndjson.xz"
            x5 = "https://storage.googleapis.com/brdata-public-data/rki-corona-archiv/2_parsed/data_2020-03-25-12-00.ndjson.xz"
            if next_url == x1 or x2 or x3 or x4 or x5:
                finished_url = write_to_file_five_and_lower.main(next_url)
            else:
                finished_url = write_to_file_after_five.main(next_url)
            delete_done_line.main(finished_url)

main()
