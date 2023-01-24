import remove_common
import get_next_url
import extract_urls
import download_url
import xz_extract
import delete_done_line
import write_to_file_after_five
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
            # if next_url =! :
            finished_url = write_to_file_after_five.main(next_url)
            delete_done_line.main(finished_url)
