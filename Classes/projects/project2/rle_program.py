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
9. Display Hex Flat Data"""


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
    # test:
    user_file = 'Image/uga.gfx'

    # access the file
    data = gfx.ConsoleGfx.load_file(user_file)

    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again

def handle_option_2():
    #print("Test option 2")
    data = gfx.ConsoleGfx.test_image
    print("Test image data loaded.")
    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again - should I do it?
def handle_option_3():
    pass
# start the program

def main():

    #1) Display welcome message
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image: ")

    #2) Display color test (ConsoleGfx.test_rainbow)
    gfx.ConsoleGfx.display_image(gfx.ConsoleGfx.test_rainbow)

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
                    handle_option_1()
                case 2:
                    #print("TEST")
                    handle_option_2()
                case 3:
                    handle_option_1()
                case 4:
                    handle_option_2()





if __name__ == "__main__":
    main()