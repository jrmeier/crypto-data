TRADING_FILE_CSV_HEADER = [
    "date",
    "close",
    "open",
    "high",
    "low",
    "volume",
]


CSV_2019_HEADER_MATCHING = {
    "date": "close_time",
    "open": "open_price",
    "close": "last_price",
    "high": "high_price",
    "low": "low_price",
    "volume": "volume",
}

# ,Date,Open,High,Low,Close,Volume,price_change,price_change_percent,weighted_avg_price,prev_close_price,last_qty,bid_price,ask_pri

OLD_2017_HEADER_MATCHING = {
    "date": 1,
    "open": 2,
    "close": 5,
    "high": 3,
    "low": 4,
    "volume": 6,
}

BINANCE_API_CSV_HEADER_MATCHING = {
    "date": "openTime",
    "open": "openPrice",
    "close": "lastPrice",
    "high": "highPrice",
    "low": "lowPrice",
    "volume": "volume",
}
