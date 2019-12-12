import logging
from ..csv_utils import format_single_row


def test_format_single_row_simple1():
    test_input_data = {
        "msg1": "Hello, tester",
        "msg2": "bye tester",
    }
    output_header = ["msg1"]
    res = format_single_row(test_input_data, output_header)

    assert res == ["Hello, tester"]


def test_format_single_row_simple2():
    test_input_data = {
        "msg1": "This is message one",
        "msg2": "Second message coming at you like",
    }
    output_header = ["msg2"]
    res = format_single_row(test_input_data, output_header)

    assert res == ["Second message coming at you like"]


def test_format_single_row_mapped1():
    output_header = ["trash_can"]
    test_input_data = {
        "keyThat_sucks": "The key for this is basically a trash can.",
    }
    header_map = {"trash_can": "keyThat_sucks"}
    res = format_single_row(test_input_data, output_header, header_map)

    assert res == ["The key for this is basically a trash can."]


def test_format_single_row_mapped2():
    output_header = ["date", "close", "open", "high", "low", "volume"]
    test_input_data = {
        "": 0,
        "Date": "2018-01-01 01:48:01",
        "Open": 12970.58,
        "High": 14050.11,
        "Low": 12425.98,
        "Close": 13380.60,
        "Volume": 11196,
        "price_change": 410.02,
        "price_change_percent": "3.161",
        "weighted_avg_price": 13272.2939873,
        "prev_close_price": 12970.58,
        "last_qty": 0,
        "bid_price": 13380.6,
        "ask_price": 13401.09,
    }

    header_map = {
        "date": "Date",
        "open": "Open",
        "close": "Close",
        "high": "High",
        "low": "Low",
        "volume": "Volume",
    }
    res = format_single_row(test_input_data, output_header, header_map)

    assert res == ["2018-01-01 01:48:01", 13380.6, 12970.58, 14050.11, 12425.98, 11196]
