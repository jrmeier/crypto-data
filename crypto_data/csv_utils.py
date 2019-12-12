def format_single_row(input_data, output_header, header_map={}):
    """ input_data: raw data 
        output_header: the header to set up as the data
        header_map: if the variables are named different than the output. See tests for documentation
    """
    # return list(map(lambda e: input_data[e], output_header))
    final = []
    for each in output_header:
        if header_map:
            try:
                final.append(input_data.get(header_map[each], None))
            except Exception as e:
                print("exception: ",e)
                pass
        else:
            try:
                final.append(input_data[each])
            except Exception as e:
                pass

    return final

