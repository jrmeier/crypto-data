# zips the files up
# from zipfile import ZipFile
import zipfile
from os import listdir
from os.path import isfile, join, dirname, abspath

def zip_the_file(zipped_file_path, file_to_zip):
    with zipfile.ZipFile(zipped_file_path,'w',) as zip:
        zip.write(file_to_zip, compress_type=zipfile.ZIP_DEFLATED) 


def daily_cron():
    # read the files in the daily_data_files
    daily_data_files_path = "{}/daily_data_files".format(dirname(abspath(__file__)))
    csv_file_paths = ["{}/{}".format(daily_data_files_path,f) for f in listdir(daily_data_files_path) if (isfile(join(daily_data_files_path, f)) & f.endswith(".csv"))]
    zipped_path = "{0}/zipped".format(dirname(abspath(__file__)))
    # zipped_path = "{}/"

    for csv_file in csv_file_paths:
        zipped_file_path = "{}/{}.zip".format(zipped_path, csv_file.split("/")[-1])

        if isfile(zipped_file_path):
            # needs to unzip and append
            with zipfile.ZipFile(zipped_file_path) as zipped:
                print(zipped)
        else:
            with zipfile.ZipFile(zipped_file_path,'w') as new_zip:

            # zip_file.extract(names,zipped_file_path)
        # zip_file.close() 
        





if __name__ == "__main__":
    daily_cron()