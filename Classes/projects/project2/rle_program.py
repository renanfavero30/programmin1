# Import libs
import console_gfx as gfx

# Data variable
data = []

# Define the menu
menu_string = """RLE Menu
--------
0. Exit
1. Load File
2. Load Test testfiles
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display testfiles
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data"""

# helper functions

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
    return result

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
    return res

def string_to_data(data_string):
    result = []
    for item in data_string:
        value = ord(item) - 87
        if value < 10:
            value = int(item)
        result.extend([value])
    return result

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

def handle_option_1():
    # ask user for file path
    #user_file = input("Enter name of file to load: ")
    # #store ConsoleGfx.load_file(filename) in image_data variable
    # test:
    user_file = 'testfiles/uga.gfx'

    # access the file
    image_data = gfx.ConsoleGfx.load_file(user_file)
    return image_data

    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again

def handle_option_2():
    # store the ConsoleGfx.test_image into image_data variable
    image_data = gfx.ConsoleGfx.test_image
    print("Test image data loaded.")
    return image_data

    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again - should I do it?
def handle_option_3():
    # Reads RLE data from the user in decimal notation with delimiters (smiley example):
    rle_data_w_delimtier = input("Enter an RLE string to be decoded: ")
    return rle_data_w_delimtier
def handle_option_4():
    # Reads RLE data from the user in hexadecimal notation without delimiters (smiley example):
    rle_data_hex = input("Enter the hex string holding RLE data: ")
    return rle_data_hex

def handle_option_5():
    pass

# start the program
def handle_option_6(image_data):
    # Displaying the testfiles
    # Displays the current image by invoking the ConsoleGfx.display_image(image_data) method.
    # display image data using ConsoleGfx.display_image(image_data)
    gfx.ConsoleGfx.display_image(image_data)
    #gfx.ConsoleGfx.display_image(gfx.ConsoleGfx.test_image)

def main():

    #1) Display welcome message
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum testfiles: ")

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
            match option:
                case 0:
                    continue_app = False
                case 1:
                    image_data = handle_option_1()
                    #print('Test1 - Done')
                case 2:
                    image_data = handle_option_2()
                    #print('Test2 - Done')
                case 3:
                    handle_option_3()
                    print('Test3 - Done')
                case 4:
                    handle_option_4()
                    print('Test4 - Done')
                case 5:
                    handle_option_5()
                    print('Test5 - Done')
                case 6:
                    handle_option_6(image_data)
                    #print('Test6 - Done')


if __name__ == "__main__":
    main()
