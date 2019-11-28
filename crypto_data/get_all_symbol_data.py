import requests

# get the data
# - api call to binance
# - get get the file


def get_all_symbol_data():
    """ gets all all ticker data for each listed symbol.
    https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#24hr-ticker-price-change-statistics
    """
    url = "https://api.binance.com/api/v3/ticker/24hr"

    return requests.get(url).json()
    # return [
    #     {
    #         "symbol": "CTXCUSDT",
    #         "priceChange": "0.00370000",
    #         "priceChangePercent": "4.022",
    #         "weightedAvgPrice": "0.09966063",
    #         "prevClosePrice": "0.09180000",
    #         "lastPrice": "0.09570000",
    #         "lastQty": "37.18000000",
    #         "bidPrice": "0.09440000",
    #         "bidQty": "1064.89000000",
    #         "askPrice": "0.09560000",
    #         "askQty": "10732.22000000",
    #         "openPrice": "0.09200000",
    #         "highPrice": "0.10870000",
    #         "lowPrice": "0.09120000",
    #         "volume": "5862325.34000000",
    #         "quoteVolume": "584243.06367600",
    #         "openTime": 1574790112015,
    #         "closeTime": 1574876512015,
    #         "firstId": 20984,
    #         "lastId": 25943,
    #         "count": 4960,
    #     }
    # ]

    return req


if __name__ == "__main__":
    res = get_all_ticker_data()

    print(res)
