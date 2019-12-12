OLD_TRADING_FILE_CSV_HEADER = [
    "last_price",
    "open_price",
    "high_price",
    "low_price",
    "price_change",
    "volume",
    "weighted_avg_price",
    "ask_price",
    "ask_qty",
    "open_time",
    "close_time",
]

TRADING_FILE_CSV_HEADER = [
    "date",
    "close",
    "open",
    "high",
    "low",
    "volume",
]

OLD_BINANCE_HEADER_MATCHING = {
    "price_change": "priceChange",
    "weighted_avg_price": "weightedAvgPrice",
    "last_price": "lastPrice",
    "ask_price": "askPrice",
    "ask_qty": "askQty",
    "open_price": "openPrice",
    "high_price": "highPrice",
    "low_price": "lowPrice",
    "volume": "volume",
    "open_time": "openTime",
    "close_time": "closeTime",
}

BINANCE_HEADER_MATCHING = {
    "date": "close_time",
    "open":"open_price",
    "close":"last_price",
    "high": "high_price",
    "low": "low_price",
    "volume": "volume"
}


OLD_2018_HEADER_MATCHING = {
    "date": "Date",
    "open": "Open",
    "close": "Close",
    "high": "High",
    "low": "Low",
    "volume": "Volume",
}

# ,Date,Open,High,Low,Close,Volume,price_change,price_change_percent,weighted_avg_price,prev_close_price,last_qty,bid_price,ask_price
# 0,2018-01-01 01:48:01,12970.58,14050.11,12425.98,13380.6,11196,410.02,3.161,13272.2939873,12970.58,0,13380.6,13401.09


AVALIABLE_MARKETS = ["BINANCE"]
