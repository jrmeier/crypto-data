import csv
import zipfile
import constants
from os import listdir, remove
from os.path import isfile, join, dirname, abspath


def unzip_file(path_to_zip, extract_dest):
    with zipfile.ZipFile(path_to_zip, 'r') as zip_file:
        zip_file.extractall(extract_dest)

def format_2018_data(old_csv_data,header=constants.OLD_2018_HEADER_MATCHING):
    new_line = []
#     OLD_2018_HEADER_MATCHING = {
#     "last_price": 5,
#     "open_price": 2,
#     "high_price": 3,
#     "low_price": 4,
#     "volume": 6,
# }
    for old_row in old_csv_data:
        # new_line.append(header['date'])
        # new_line.append(old_row[header['last_price']])
        # new_line.append()
        # print(lp)
    
    return new_line    

def convert_2018_file(old_csv_path, new_csv_path):
    # get the old data
    with open(old_csv_path, 'r') as my_file:

        reader = csv.reader(my_file, delimiter=',')
        old_csv_data = list(reader)[1:]

    # put the data in the new format

    formatted_data = format_2018_data(old_csv_data)    
    print(formatted_data)
    # with open(new_csv_path, "w+") as new_file:
    #     file_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)




if __name__ == "__main__":
    # path_to_zip="BTCUSDT.csv.zip"
    # extract_dest="./crypto_data/tmp"

    old_csv_path = "./crypto_data/tmp/BTCUSDT_sample.csv"
    new_csv_path = ""
    convert_2018_file(old_csv_path, new_csv_path)

