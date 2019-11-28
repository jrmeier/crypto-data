TRADING_FILE_CSV_HEADER = [
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

BINANCE_HEADER_MATCHING = {
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

AVALIABLE_MARKETS = [
    "BINANCE"
]