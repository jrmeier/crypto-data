import zipfile
import os
import csv


def open_csv_file(csv_path):
    with open(csv_path, "r") as my_file:
        reader = csv.reader(my_file, delimiter=",")
        return list(reader)[1:]


def daily_cron(daily_csv_path, zipped_path):
    daily_csv_path = os.path.abspath(daily_csv_path)

    csv_file_paths = [
        "{}/{}".format(daily_csv_path, f)
        for f in os.listdir(daily_csv_path)
        if (os.path.isfile(os.path.join(daily_csv_path, f)) & f.endswith(".csv"))
    ]
    zipped_path = os.path.abspath(zipped_path)

    for csv_file in csv_file_paths:
        new_arcname = "{}.csv".format(csv_file.split("/")[-1].split("_")[0])
        zipped_file_path = "{}/{}.zip".format(zipped_path, new_arcname)
        archived_csv_path = "{}/{}".format(zipped_path, new_arcname)

        if os.path.isfile(zipped_file_path):
            with zipfile.ZipFile(zipped_file_path, "r") as zip_ref:
                zip_ref.extractall(zipped_path)
            with open(archived_csv_path, "a+", newline="") as archive_csv_file:
                csv_writer = csv.writer(archive_csv_file)
                lines = open_csv_file(csv_file)
                csv_writer.writerows(lines)

            os.remove(zipped_file_path)

            with zipfile.ZipFile(zipped_file_path, "w") as new_zip:
                new_zip.write(
                    archived_csv_path, compress_type=zipfile.ZIP_DEFLATED, arcname=new_arcname,
                )

            os.remove(archived_csv_path)
            os.remove(csv_file)

        else:
            with zipfile.ZipFile(zipped_file_path, "w") as new_zip:
                new_zip.write(csv_file, compress_type=zipfile.ZIP_DEFLATED, arcname=new_arcname)
            os.remove(csv_file)


if __name__ == "__main__":
    daily_csv_path = "./crypto_data/daily_csvs"
    zipped_path = "./crypto_data/zipped"
    daily_cron(daily_csv_path, zipped_path)
