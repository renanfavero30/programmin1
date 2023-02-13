def octal_string_decode (oct):
    if oct[0] == "0":
        oct = oct[1:]
    left_most_bit_index = len(oct) - 1
    res= 0
    for digit in oct:
        res += int(digit) * 8 ** left_most_bit_index
        left_most_bit_index -= 1
    return res



hex ="0x12E"
if hex[0] == 0 and hex[1] == "x":
    hex = hex[2:]
    print(hex)

if __name__ =='__main__':
    print(octal_string_decode('123'))