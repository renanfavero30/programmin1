def to_rle_string(rle_data):
    result = ""
    #rle_data = "".join([char for char in rle_data if char.isdigit()])
    # for each run, display run lengh in decima(2digits) and the run value in hexadecimal 1 digit, delimited by :
    for i in range(0, len(rle_data)-1, 2):
        decimal = (rle_data[i])
        hexadecimal = (rle_data[i + 1])
        if int(hexadecimal) > 9:
            hexadecimal = str(chr(hexadecimal + 87))  # transform in hexa
        pair = (f':{decimal}{hexadecimal}')
        result += pair
    rle_string = result[1:]
    return rle_string


rle_data = [3, 15, 6, 4]
print(to_rle_string(rle_data))