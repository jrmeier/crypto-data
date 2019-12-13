import re
import time
import datetime


def format_single_row(input_data, output_header, header_map={}):
    """ input_data: raw data
        output_header: the header to set up as the data
        header_map: if the variables are named different than the output
    """

    row = []
    for each in output_header:
        if header_map:
            try:
                # dp = str(input_data.get(header_map[each]))
                dp = input_data[header_map[each]]
                if each == "date" and re.match("\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}", dp):  # noqa
                    dp = int(
                        time.mktime(datetime.datetime.strptime(dp, "%Y-%m-%d %H:%M:%S").timetuple())
                    )
                row.append(dp)
            except Exception:
                # do some logging
                pass
        else:
            try:
                row.append(input_data[header_map[each]])
            except Exception:
                # do some logging
                pass

    return row
# def format_single_row(input_data, output_header, header_map={}):


if __name__ == "__main__":
    input_data = {"name": "jed","age":25,"happy": True}
    input_data = ["jed","25",True]
    output_header = ["first_name","age", "happy"]
    header_map = {"first_name": 0,"age":1, "happy":2}

    res = format_single_row(input_data, output_header, header_map)
    print(res)