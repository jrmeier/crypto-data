import os
import csv
import constants


def get_file_path(symbol=None):
    """ 
    Creates a new file or returns the existing file

    Returns new file path
     """
    if not symbol:
        return None

    file_path = "{}/daily_data_files/{}_daily.csv".format(os.path.dirname(os.path.abspath(__file__)), symbol)
    # return file_path
    if os.path.exists(file_path):
        return file_path

    with open(file_path, "w+") as new_file:
        file_writer = csv.writer(new_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)

    return file_path


def append_to_file(symbol, data_row):
    """ appends a raw data row to the file """
    symbol_file_path = get_file_path(symbol)

    formatted_data_row = create_formatted_data_row(data_row)
    with open(symbol_file_path, "a") as opened_file:
        file_writer = csv.writer(opened_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(formatted_data_row)

    return "{} updated. ".format(symbol_file_path)


def create_formatted_data_row(input_data, header=constants.BINANCE_HEADER_MATCHING):
    new_line = []
    for column in constants.TRADING_FILE_CSV_HEADER:
        data_point = input_data.get(header[column])
        try:
            data_point = int(data_point)
        except ValueError:
            pass

        new_line.append(data_point)

    return new_line
