
import console_gfx as gfx

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

def main():

    #1) Display welcome message
    print("Welcome to the RLE image encoder!")
    print()
    print("Displaying Spectrum Image: ")
    #2) Display color test (ConsoleGfx.test_rainbow)
    gfx.ConsoleGfx.display_image(gfx.ConsoleGfx.test_rainbow)
    #3) Display the menu
    print(menu_string)
    option = input('Select a Menu Option: ')
    if not is_input_valid(option):
        # in the case that the input is bad
        #can ask the user to enter the input again
        pass
    else
        # do the thing that they asked
        match option:
            case 0:
                exit
            case 1:
                handle_option_1()
                pass



#Error! Invalid input.")
    #4) Prompt for input

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
    user_file = input("Enter name of file to load: ")

    # try to access the file
    gfx.load_file(user_file)

    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again

def handle_option_2():
    # load test file
    gfx.load_file(gfx.test_image)

    # if success then tell the user and display menu again
    # save the file after getting the user input

    # if fail then tell user and display menu again
def handle_option_2():
    pass

if __name__ == "__main__":
    main()