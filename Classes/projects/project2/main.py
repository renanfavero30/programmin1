def to_hex_string(data):
    # Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging.
    # Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64".
    result = ""
    for number in data:
        if number > 9:
            result += str(chr(number + 87))  # transform in hexa
        else:
            result += str(number)

    return result

#print(to_hex_string([3,15,6,4]))

def count_runs(arr):
    runs = 1 # how may runs
    repetitions = 1
    current = arr[0]
    for num in arr[1:]:
        if current == num:  # if is the same number
            repetitions += 1
        else:
            current = num  #
            repetitions = 1  # restart the repetitions
            runs += 1
        if repetitions > 15:  # max number of pixel per run
            repetitions = 1  #
            runs += 1
    return runs

#print(count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7 ]))
#print(count_runs([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))

def encode_rle(flat_data):
#Returns encoding (in RLE) of the raw data passed in; used to generate RLE representation of a data.
#Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4].
    index = 0
    repetitions = 1
    result = []
    current = flat_data[0]
    for num in flat_data[1:]:
        index += 1
        if current == num:  # if is the same number
            repetitions += 1
            if repetitions > 15:
                result.extend([15, current])
                repetitions = 1
        else:
            result.extend([repetitions, current])
            current = num  #
            repetitions = 1  # restart the repetitions
        if index == len(flat_data)-1:
            result.extend([repetitions, current])
    return result


#print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]))
"""
· input: [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]
· output: [2,4,15,1,15,1,5,1,1,8,1,7]

· input: [1,2,3,4,1,2,3,4]
· output: [1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,4]

· input: [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
· output: [2,4,15,1,15,1,5,1]

· input: [4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
· output: [1,4,1,5,15,1,15,1,5,1]
"""
#print(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]))
#print(encode_rle([1,2,3,4,1,2,3,4]))
#print(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
#print(encode_rle([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

def get_decoded_length(rle_data):
# Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2)
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9.
    result = 0
    for index, nro in enumerate(rle_data):
        if index % 2 == 0:
            result += nro
    return result

#print(get_decoded_length([3, 15, 6, 4]))



def decode_rle(rle_data):
#Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3)
#Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4].
    res=[]
    for idx in range(0, len(rle_data), 2):
        value = rle_data[idx + 1]
        repetitions = rle_data[idx]
        res.extend([value] * repetitions)
    return res

#print(decode_rle([3, 15, 6, 4]))
"""
· input: [2,4,15,1,15,1,5,1,1,8,1,7]
· output: [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]
"""
#print(decode_rle([2,4,15,1,15,1,5,1,1,8,1,7]))

def string_to_data(data_string):
    result = []
    for item in data_string:
        value = ord(item) - 87
        if value < 10:
            value = int(item)
        result.extend([value])
    return result

#print(string_to_data("3f64"))

# def string_to_rle(rle_string):
#     result = []
#     parts = rle_string.split(':')
#     for part in parts:
#         run = int(part[:-1])
#         value = part[-1]
#         run_value = ord(value) - 87
#         if run_value < 10:
#             run_value = int(value)
#         result.extend([run, run_value])
#     return result

#print(string_to_data("15f:64"))
#print(string_to_data("151:14a:13f:1a:9f:55"))
