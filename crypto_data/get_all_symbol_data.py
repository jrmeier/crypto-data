import requests


def get_all_symbol_data():
    """ gets all all ticker data for each listed symbol.
    https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#24hr-ticker-price-change-statistics
    """
    url = "https://api.binance.com/api/v3/ticker/24hr"

    return requests.get(url).json()


if __name__ == "__main__":
    res = get_all_ticker_data()

    print(res)
