# zips the files up
import zipfile
from os import listdir
from os.path import isfile, join, dirname, abspath
# os.path.dirname(os.path.abspath(__file__))


def daily_cron():
    # read the files in the daily_data_files
    daily_data_files_path = "{}/daily_data_files/".format(dirname(abspath(__file__)))
    zipped_files_path = {}
    daily_files = [f for f in listdir(daily_data_files_path) if isfile(join(daily_data_files_path, f))]

    # zip = zipfile.ZipFile(loczip, "w", zipfile.ZIP_DEFLATED)

    for daily_file in daily_files:
        file_path_to_zip = "{}{}".format(daily_data_files_path, daily_file)
        # print(file_path_to_zip)
        # zipfile.ZipFile(file_path_to_zip, "w", zipfile.ZIP_DEFLATED)



if __name__ == "__main__":
    daily_cron()