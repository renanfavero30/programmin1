from console_gfx import ConsoleGfx

ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

# welcme
# dispmlay spectruim

image_data = None

while True:
    # print all menu options
    # prompt the user for menu option
    option = int(input("select  mmenu option"))
    # set up option 0, 1, 2, 6
    if option == 0:
        break
    elif option ==1:
        #prompt the filename entenred by user
        #store ConsoleGfx.load_file(filename) in image_data variable
    elif option ==2:
        # store the ConsoleGfx.test_image into image_data variable
    elif option == 6:
        #display image data using ConsoleGfx.display_image(image_data)
        pass