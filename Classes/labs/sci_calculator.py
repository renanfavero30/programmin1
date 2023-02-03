# Renan Favero
# LAB 03

#impor lib
import math

# start with result accumulated = 0
n = 0
accumulated_result = 0

# initial resul
nro3 = 0.0

# print Current Result:
print(f"Current Result: {nro3}")

# set initial option != 0
option = 2

# Loop to show the menu n times
while option != 0:
    # Insert the menu
    print(f"Calculator Menu\n"
            f" ---------------\n"
            f" 0. Exit Program \n"
            f" 1. Addition \n"
            f" 2. Subtraction \n"
            f" 3. Multiplication  \n"
            f" 4. Division\n"
            f" 5. Exponentiation\n"
            f" 6. Logarithm\n"
            f" 7. Display Average\n"
            f"\n"
            )
    # initial boolean variable
    error = True
    while error == True:
        option = int(input("Enter Menu Selection: "))

        # when iser what exit types 0
        if option == 0:
            print("Thanks for using this calculator. Goodbye!")
            exit()

        # if n = 0 there is no average
        if option == 7 and n == 0:
            print("Error: No calculations yet to average!")
            error = True
            continue

        #If an option with operands (1-6) is selected, the program should prompt for and read floating point
        elif option >=1 and option <= 6:
            error = False

            # Set the inputs values to calculate
            nro1 = input("Enter first operand: ")
            # To Receive extra credit - check if input = RESULT so input = nro3
            if nro1 == 'RESULT':
                nro1 = nro3
            else:
                nro1 = float(nro1)
            #nro1 = float(input(f"Enter first operand: "))
            #nro2 = float(input(f"Enter second operand: "))

            nro2 = input("Enter second operand: ")
            # To Receive extra credit - check if input = RESULT so input = nro3
            if nro2 == 'RESULT':
                nro2 = nro3
            else:
                nro2 = float(nro2)

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
                nro3 = math.log(nro2, nro1)

            # Round result to two decimals
            if type(nro1) or type(nro2) == nro3:
                nro3 = round(nro3, 3)
            else:
                nro3 = round(nro3, 2)

            # Count the nro of calculations
            n += 1

            # Save accumulated results
            accumulated_result += nro3

            # Calculate the average
            average = round((accumulated_result/n), 2)

            # Output the result
            print(f'Current Result: {nro3}')

        elif option == 7:
            print(f"Sum of calculations: {accumulated_result}\n"
                  f"Number of calculations: {n}\n"
                  f"Average of calculations: {average} ")

        else:
            print('Error: Invalid selection!')
            error = True

