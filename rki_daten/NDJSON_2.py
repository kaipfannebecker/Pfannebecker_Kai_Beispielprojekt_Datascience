#!/usr/bin/env python3
#
# ndjson_to_csv.py
#
# Author: Werner Robitza
#
# Convert .ndjson files to CSV.
# This assumes the same keys being used in every line of the input file.
# It works on a line-by-line basis, so it should be fast and memory-efficient.

import json
import argparse
import csv
from tqdm import tqdm


def convert_to_csv(ndjson_file, csv_file):
    with open(ndjson_file, "r") as in_f:
        with open(csv_file, "w") as out_f:
            writer = csv.writer(out_f, quoting=csv.QUOTE_NONNUMERIC)
            wrote_headers = False
            data_len = None
            for line in tqdm(in_f):
                if line.strip() == "":
                    continue
                data = json.loads(line.strip())
                sorted_data = sorted(data.items())

                if data_len is None:
                    data_len = len(sorted_data)

                # skip error lines
                if len(sorted_data) != data_len:
                    print("Warning: different keys in line: {}".format(line))
                    continue

                # replace empty values
                for key in data.keys():
                    if data[key] is None:
                        data[key] = ""

                if not wrote_headers:
                    writer.writerow([k for k, v in sorted_data])
                    wrote_headers = True

                writer.writerow([v for k, v in sorted_data])


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("input", help="input data_2020-03-21-12-00.ndjson")
    parser.add_argument("output", help="output .csv")
    cli_args = parser.parse_args()

    convert_to_csv(cli_args.input, cli_args.output)


if __name__ == "__main__":
    main()