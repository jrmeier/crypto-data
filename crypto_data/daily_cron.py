# zips the files up
# from zipfile import ZipFile
import zipfile
from os import listdir, remove
from os.path import isfile, join, dirname, abspath
import csv

def open_csv_file(csv_path):
    with open(csv_path, 'r') as my_file:
        reader = csv.reader(my_file, delimiter=',')
        return list(reader)[1:]


def daily_cron():
    # read the files in the daily_data_files
    daily_data_files_path = "{}/daily_data_files".format(dirname(abspath(__file__)))
    csv_file_paths = ["{}/{}".format(daily_data_files_path,f) for f in listdir(daily_data_files_path) if (isfile(join(daily_data_files_path, f)) & f.endswith(".csv"))]
    
    zipped_path = "{0}/zipped".format(dirname(abspath(__file__)))

    for csv_file in csv_file_paths:
        new_arcname = "{}.csv".format(csv_file.split("/")[-1].split("_")[0])

        zipped_file_path = "{}/{}.zip".format(zipped_path, new_arcname)
        
        archived_csv_path = "{}/{}".format(zipped_path, new_arcname)


        if isfile(zipped_file_path):
            # needs to unzip and append
            with zipfile.ZipFile(zipped_file_path, 'r') as zip_ref:
                zip_ref.extractall(zipped_path)
            with open(archived_csv_path, "a+", newline='') as archive_csv_file:
                print("appending to: ", archived_csv_path)
                csv_writer = csv.writer(archive_csv_file)
                lines = open_csv_file(csv_file)
                csv_writer.writerows(lines)
            
            remove(zipped_file_path)

            with zipfile.ZipFile(zipped_file_path,'w') as new_zip:
                 new_zip.write(archived_csv_path, compress_type=zipfile.ZIP_DEFLATED, arcname=new_arcname)

            
            remove(archived_csv_path)
            remove(csv_file)
            
        else:
            print("need to create a new zipped ")
            with zipfile.ZipFile(zipped_file_path,'w') as new_zip:
                new_zip.write(csv_file, compress_type=zipfile.ZIP_DEFLATED, arcname=new_arcname)
            remove(csv_file)



if __name__ == "__main__":
    daily_cron()