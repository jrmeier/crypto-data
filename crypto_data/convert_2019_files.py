import csv
import zipfile
import constants
import os
import csv_utils

def convert_single_2019_file(old_zip_path, new_zipped_location):
    # unzip the old file
    with zipfile.ZipFile(old_zip_path, "r") as zip_file:
        zip_file.extractall(new_zipped_location)

    # get the old data
    # new_file_path = old_zip_path.split(".zip")[0]
    tmp_csv_filename = old_zip_path.split("/")[-1].split(".zip")[0]
    
    new_file_path = os.path.abspath("{}/{}".format(new_zipped_location, tmp_csv_filename))
    
    with open(new_file_path, "r") as my_file:
        reader = csv.DictReader(my_file, delimiter=",")
        old_csv_data = list(reader)
        new_file_name = my_file.name.split("/")[-1]

    formatted_rows = list(map(lambda x: csv_utils.format_single_row(x, constants.TRADING_FILE_CSV_HEADER, constants.BINANCE_HEADER_MATCHING), old_csv_data))

    new_csv_path = "{}/{}".format(new_zipped_location, new_file_name)
    
    with open(new_csv_path, "w+") as new_file:
        file_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)
        file_writer.writerows(formatted_rows)
    
    #zip the file
    standard_zipped_location = "{}/{}.zip".format(new_zipped_location, new_file_name)
    # print("standard_zipped_location: ", standard_zipped_location)
    with zipfile.ZipFile(standard_zipped_location, "w") as new_zip:
        new_zip.write(
            new_csv_path, compress_type=zipfile.ZIP_DEFLATED, arcname=new_file_name,
        )

    print("writing new file at: ",standard_zipped_location)
    #delete the old csv's
    print("removing: {}".format(new_csv_path))
    os.remove(new_csv_path)
    

def convert_2019_files(old_zip_path, new_zip_path):
    # list all the files in the dir
    
    for zipped_file in os.listdir(old_zip_path):
        if zipped_file.endswith(".zip"):
            # print(zipped_file)
            # print(os.path.abspath(new_zip_path))
            single_zippled_path = "{}/{}".format(os.path.abspath(old_zip_path), zipped_file)
            convert_single_2019_file(single_zippled_path, new_zip_path)
            # print("single zipped path: ",single_zippled_path)

    # convert each file
    


if __name__ == "__main__":
    # path_to_zip="BTCUSDT.csv.zip"
    # extract_dest="./crypto_data/tmp"

    # old_csv_path = "./crypto_data/zipped/ADABNB.csv.zip"
    # new_zipped_location = './crypto_data/2019_standard/'
    # res = convert_single_2019_file(old_csv_path, new_zipped_location)

    old_zip_path = "./crypto_data/azipped_old"
    new_zip_path = "./crypto_data/2019_standard"
    res = convert_2019_files(old_zip_path, new_zip_path)
    print(res)
