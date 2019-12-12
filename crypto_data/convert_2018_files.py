import csv
import zipfile
import constants
from os import listdir, remove
from os.path import isfile, join, dirname, abspath

import csv_utils


def unzip_file(path_to_zip, extract_dest):
    with zipfile.ZipFile(path_to_zip, "r") as zip_file:
        zip_file.extractall(extract_dest)



def convert_2018_file(old_csv_path, new_csv_path):
    # get the old data
    with open(old_csv_path, "r") as my_file:
        reader = csv.DictReader(my_file, delimiter=",")
        old_csv_data = list(reader)

    formatted_rows = list(map(lambda x: csv_utils.format_single_row(x, constants.TRADING_FILE_CSV_HEADER, constants.OLD_2018_HEADER_MATCHING), old_csv_data))

    with open(new_csv_path, "w+") as new_file:
        file_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)
        file_writer.writerows(formatted_rows)


if __name__ == "__main__":
    # path_to_zip="BTCUSDT.csv.zip"
    # extract_dest="./crypto_data/tmp"

    old_csv_path = "./crypto_data/tmp/BTCUSDT_sample.csv"
    new_csv_path = "./crypto_data/tmp/BTCUSDT_sample_NEW.csv"
    convert_2018_file(old_csv_path, new_csv_path)