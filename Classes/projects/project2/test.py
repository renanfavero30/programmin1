rle_data = [15, 15, 6, 4]
result = ""
# for each run, display run lengh in decima(2digits) and the run value in hexadecimal 1 digit, delimited by :
for i in range(0, len(rle_data), 2):
    decimal = (rle_data[i])
    hexadecimal = (rle_data[i + 1])
    if hexadecimal > 9:
        hexadecimal = str(chr(hexadecimal + 87))  # transform in hexa
    pair = (f':{decimal}{hexadecimal}')
    result += pair
result = result[1:]
