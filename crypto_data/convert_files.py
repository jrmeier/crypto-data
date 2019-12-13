import csv
import zipfile
import constants
import os
import csv_utils


def convert_single_file(old_zip_path, new_zip_dir, header_match):
    # unzip the old file

    with zipfile.ZipFile(old_zip_path, "r") as zip_file:
        zip_file.extractall(new_zip_dir)
    # get the old data

    tmp_csv_filename = old_zip_path.split("/")[-1].split(".zip")[0]

    new_file_path = os.path.abspath("{}/{}".format(new_zip_dir, tmp_csv_filename))

    # return new_file_path
    with open(new_file_path, "r") as my_file:
        reader = csv.reader(my_file)
        #skip the header
        next(reader)
        old_csv_data = list(reader)
        new_file_name = my_file.name.split("/")[-1]

    formatted_rows = list(
        map(
            lambda x: csv_utils.format_single_row(
                x, constants.TRADING_FILE_CSV_HEADER, header_match
            ),
            old_csv_data,
        )
    )

    new_csv_path = "{}/{}".format(new_zip_dir, new_file_name)

    with open(new_csv_path, "w+") as new_file:
        file_writer = csv.writer(new_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)
        file_writer.writerows(formatted_rows)

    # zip the file
    standard_zipped_location = "{}/{}.zip".format(new_zip_dir, new_file_name)
    with zipfile.ZipFile(standard_zipped_location, "w") as new_zip:
        new_zip.write(
            new_csv_path, compress_type=zipfile.ZIP_DEFLATED, arcname=new_file_name,
        )

    print("writing new file at: ", standard_zipped_location)
    # removing the temp csv
    print("removing: {}".format(new_csv_path))
    # os.remove(new_csv_path)


def convert_files(old_zip_dir, new_zip_dir, header_match):
    # list all the files in the dir
    if not os.path.exists(new_zip_dir):
        os.makedirs(new_zip_dir)

    for zipped_file in os.listdir(old_zip_dir):
        if zipped_file.endswith(".zip"):
            single_zippled_path = "{}/{}".format(os.path.abspath(old_zip_dir), zipped_file)
            res = convert_single_file(single_zippled_path, new_zip_dir, header_match)
            # print(res)


if __name__ == "__main__":
    # 2019 files
    # old_zip_path = "./crypto_data/2019_zipped_sample"
    # new_zip_path = "./crypto_data/2019_standard"
    # header_match = constants.CSV_2019_HEADER_MATCHING

    # 2018 files
    old_zip_path = "./crypto_data/2017_zipped/"
    # print(old_zip_path)

    new_zip_dir = "./crypto_data/2017_standard/"
    header_match = constants.OLD_2017_HEADER_MATCHING

    res = convert_files(old_zip_path, new_zip_dir, header_match)


    print(res)
