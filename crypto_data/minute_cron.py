import os
import csv
import constants
import csv_utils
import requests
import json


def create_file_path(symbol, csv_path):
    """
    Creates a new file or returns the existing file
    """

    file_path = "{}/{}_daily.csv".format(os.path.abspath(csv_path), symbol)

    if os.path.exists(file_path):
        return file_path

    with open(file_path, "w+") as new_file:
        file_writer = csv.writer(new_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(constants.TRADING_FILE_CSV_HEADER)

    return file_path


def append_to_file_csv(symbol, data_row, csv_path):
    """ appends a raw data row to the file """
    symbol_file_path = create_file_path(symbol, csv_path)
    formatted_data_row = csv_utils.format_single_row(
        data_row, constants.TRADING_FILE_CSV_HEADER, constants.BINANCE_API_CSV_HEADER_MATCHING
    )

    with open(symbol_file_path, "a") as opened_file:
        file_writer = csv.writer(
            opened_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file_writer.writerow(formatted_data_row)

    return "{} updated. ".format(symbol_file_path)


def get_all_symbol_data():
    """ gets all all ticker data for each listed symbol.
    https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#24hr-ticker-price-change-statistics
    """
    url = "https://api.binance.com/api/v3/ticker/24hr"

    return requests.get(url).json()


def minute_cron(csv_path):
    for ticker_data in get_all_symbol_data():
        append_to_file_csv(ticker_data.get("symbol", None), ticker_data, csv_path)
        # print(append_to_file_csv("ADABNB", ticker_data, csv_path))


if __name__ == "__main__":
    csv_path = "./crypto_data/daily_csvs"
    minute_cron(csv_path)
