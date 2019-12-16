TRADING_FILE_CSV_HEADER = [
    "date",
    "close",
    "open",
    "high",
    "low",
    "volume",
]


CSV_2019_HEADER_MATCHING = {
    "date": 10,
    "open": 1,
    "close": 0,
    "high": 2,
    "low": 3,
    "volume": 5,
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

#    0            1       2           3           4           5       6                   7       8       9           10
# last_price,open_price,high_price,low_price,price_change,volume,weighted_avg_price,ask_price,ask_qty,open_time,close_time
# 7525.50000000,7699.25000000,7810.00000000,7441.00000000,-173.75000000,46477.74085300,7644.13869416,7525.81000000,0.08886500,1575063841610,1575150241610