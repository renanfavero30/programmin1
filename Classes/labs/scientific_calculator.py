# Renan Favero
# LAB 03

#impor lib
import math

#Initial option
option = 0

#start with result accumulated = 0
n = 0
accumulated_result = 0

nro3 = 0

#print Current Result:
print(f"Current Result: {nro3}")

option = 2

# Loop to show the menu n times
while option != 0:
    # Insert the menu
    option = int(input(
                       f"Calculator Menu\n"
                       f" ---------------\n"
                       f" 0. Exit Program \n"
                       f" 1. Addition \n"
                       f" 2. Subtraction \n"
                       f" 3. Multiplication  \n"
                       f" 4. Division\n"
                       f" 5. Exponentiation\n"
                       f" 6. Logarithm\n"
                       f" 7. Display Average\n"
                       ))
    if option == 0:
        print("Thanks for using this calculator. Goodbye!")
        exit()

    # if n = 0 there is no average
    if option == 7 and n == 0:
        print("Error: No calculations yet to average!")


    #If an option with operands (1-6) is selected, the program should prompt for and read floating point
    elif option >=1 or option <= 6:
        nro1 = float(input(f"Enter first operand: "))
        nro2 = float(input(f"Enter second operand: "))

    # Calculate the result
        if option == 1:
            nro3 = nro1 + nro2
        elif option == 2:
            nro3 = nro1 - nro2
        elif option == 3:
            nro3 = nro1 * nro2
        elif option == 4:
            if nro2 == 0:
                print("Error: Invalid selection! Terminating program.")
                exit()
            else:
                nro3 = nro1 / nro2
        elif option == 5:
            nro3 = nro1 ** nro2
        elif option == 6:
            nro3 = math.log(nro1, nro2)
        elif option == 7:
            print(f"Sum of calculations: {accumulated_result}\n"
              f"Number of calculations: {n}\n"
              f"Average of calculations: {average} ")

        # Arround result to two decimals
        nro3 = round(nro3, 2)

        #count the nro of calculations
        n += 1

        # Save accumulated results
        accumulated_result += nro3

        # calculate the average
        average = round((accumulated_result/n), 2)

        # Output the result
        print(f'Current Result: {nro3}. Goodbye!')
        continue