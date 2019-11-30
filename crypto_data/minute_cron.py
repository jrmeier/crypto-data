from get_all_symbol_data import get_all_symbol_data
from manage_file import append_to_file

def minute_cron():
    for ticker_data in get_all_symbol_data():
        append_to_file(ticker_data.get("symbol",None), ticker_data)
        # print(append_to_file("ADABNB", ticker_data))

if __name__ == "__main__":
    minute_cron()