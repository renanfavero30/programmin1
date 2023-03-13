# Import libs
import console_gfx as gfx

# Data variable
data = []

# Define the menu
menu_string = """RLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
"""

# helper functions

def to_hex_string(data):
    # Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging.
    # Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64".
    hex_string = ""
    for number in data:
        if number > 9:
            hex_string += str(chr(number + 87))  # transform in hexa
        else:
            hex_string += str(number)
    data_string = hex_string
    return data_string


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
        encoded_flat_data = result
    return encoded_flat_data

def get_decoded_length(rle_data):
# Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2)
# Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9.
    result = 0
    for index, nro in enumerate(rle_data):
        if index % 2 == 0:
            result += nro
    return result

def decode_rle(rle_data):
#Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3)
#Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4].
    res=[]
    for idx in range(0, len(rle_data), 2):
        value = rle_data[idx + 1]
        repetitions = rle_data[idx]
        res.extend([value] * repetitions)
        flat_data = res
    return flat_data

def string_to_data(data_string):
    result = []
    for item in data_string:
        value = ord(item) - 87
        if value < 10:
            value = int(item)
        result.extend([value])
        rle_data = result
    return rle_data

def string_to_rle(rle_string):
    result = []
    parts = rle_string.split(':')
    for part in parts:
        run = int(part[:-1])
        value = part[-1]
        run_value = ord(value) - 87
        if run_value < 10:
            run_value = int(value)
        result.extend([run, run_value])
    return result

def to_rle_string(rle_data):
    #rle_data = [15, 15, 6, 4]
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

"""
This function should return a boolean 
"""
def is_input_valid(input):
    if input.isdigit():
        number = int(input)
        return number >= 0 and number <= 9
    return False

def handle_option_0():
    pass

def main():

    #1) Display welcome message
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image: ")

    #2) Display color test (ConsoleGfx.test_rainbow)
    gfx.ConsoleGfx.display_image(gfx.ConsoleGfx.test_rainbow)

    image_data = []

    continue_app = True
    while continue_app:
        #3) Display the menu
        print(menu_string)

        # Input the option selected
        option = input('Select a Menu Option: ')

        # If the option is not valid:
        if not is_input_valid(option):
            # in the case that the input is bad
            print('Error! Invalid input')

        # If the options is valid:
        else:
            # Transform to a int number
            option = int(option)

        # Handle the menu options
        if option == 0:
            continue_app = False

        elif option == 1:
            user_file = input("Enter name of file to load: ")
            image_data = gfx.ConsoleGfx.load_file(user_file)
            # return image_data
            #print('Test1 - Done')

        elif option == 2:
            image_data = gfx.ConsoleGfx.test_image
            print("Test image data loaded.")
            # return image_data
            #print('Test2 - Done')

        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            decode_data = decode_rle(rle_data)
            #print(decode_data)
            # print('Test3 - Done')

        elif option == 4:
            rle_string_data = input("Enter the hex string holding RLE data: ")
            rle_data = string_to_data(rle_string_data)
            decode_data = decode_rle(rle_data)
            # print(rle_data)
            # print('Test4 - Done')

        elif option == 5:
            data_string = input("Enter the hex string holding flat data: ")
            decode_data=to_rle_string(data_string)
            # print('Test5 - Done')

        elif option == 6:
            print("Displaying image...")
            gfx.ConsoleGfx.display_image(image_data)
            # print('Test6 - Done')

        elif option == 7:
            encode = encode_rle(decode_data)
            rle_string = to_rle_string(encode)
            print(f"RLE representation: {rle_string}")
            # print('Test7 - Done')

        elif option == 8:
            encode = encode_rle(decode_data)
            rle = to_hex_string(encode)
            print(f"RLE hex values: {rle}")
            # print('Test8 - Done')

        elif option == 9:
            rle = to_hex_string(decode_data)
            print(f"Flat hex values: {rle}")


if __name__ == "__main__":
    main()
