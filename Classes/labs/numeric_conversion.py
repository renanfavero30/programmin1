#if __name__ == "__main__":
 #   main()

# FUNCTIONS:

# If the character is not a letter  it will be integer, otherwise it will transform to decimal using the ASCII table
def hex_char_decode(digit):
    number = digit
    if not number.isalpha():
        number = int(number)
    else:
        number = int(ord(number.upper()) - 55)
    return number

def hex_string_decode(hex):
    # Include the input in the function
    number_input = str(hex)

    # Shows an example
    #Decodes a single hexadecimal digit and returns its value.
    # 7CF = (7 × 16^2) + (12 × 16^1) + (15 × 16^0)
    # A15 = 2581

    # Exclude the prefix if it has
    #list[first_index:last_index+1]
    number_input[]
    number_input[0:2]
    number_input = number_input.removeprefix('0x')
    i = 1
    total = 0
    # create a loop for each character:
    for element in range(0, len(str(number_input)), 1):
        # Select one element of input
        number = (number_input[element])
        # Apply the function created to convert a character to decimal
        number = hex_char_decode(number)
        # Calculate the total digits in the nro
        numb_of_digits = int(len(str(number_input)))
        # Calculate the power for each nro
        power = int(numb_of_digits - i)
        # print the total
        total += number * (16 ** power)
        i += 1
    return(total)


# Decodes a binary string and returns its value.
def binary_string_decode(binary):
    number_input = str(binary)
    # Exclude the prefix if it has
    number_input = number_input.removeprefix('0b')
    i = 0
    total = 0
    # create a loop for each character:
    for element in range(0, len(str(number_input)), 1):
        # Select one element of input
        number = (number_input[element])
        # Calculate the total digits in the nro
        numb_of_digits = int(len(str(number_input)))
        # Calculate the power for each nro
        power = int(numb_of_digits - (i+1))
        # print the total
        total += (2 ** power ) * int(number)
        i += 1
    return total
#print(f"binary {binary_string_decode(101010)}")
def dec_to_hex(dechimal_nums):
    hexa = "0b"
    stop = 0
    temp = int(dechimal_nums)
    while stop == 0:
        reminder = temp % 16 # Modulo - reminder transfor in hexa
        temp = (int(temp) // 16)  # Quociente - temp for continue
        if temp >0:
            if reminder > 9:
                reminder = (chr(reminder + 55)) # transform in hexa
            hexa = ("".join([str(reminder), str(hexa)]))
        else:
            if reminder > 9:
                reminder = (chr(reminder + 55)) # transform in hexa
            hexa = ("".join([str(reminder), str(hexa)]))
            hexa = hexa[:-1]
            print(hexa)
            stop = 1
    return hexa

#Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
def binary_to_hex(binary):
    decode = binary_string_decode(binary)
    print(f'decode= {decode}')
    number =  dec_to_hex(decode)
    return number

# Tests
#print(f'binary = {decode}')
#print(f'hex = {binary_to_hex(101010)}')


def main():

    close = 0
    while close == 0:
        option = int(input(f"Decoding Menu\n"
              " -------------\n"
              "1. Decode hexadecimal\n" 
              "2. Decode binary\n"
              "3. Convert binary to hexadecimal\n" 
              "4. Quit\n"
              "\n" 
              "Please enter an option: "))

        # Calculate the result
        if option == 1:
            number_input = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(number_input)
        elif option == 2:
            number_input = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(number_input)
        elif option == 3:
            number_input = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(number_input)
        elif option == 4:
            print("Goodbye!")
            exit()
        else:
            print("Error: Invalid selection! Terminating program.")
            exit()

        # Output the result
        print(f'Result: {result}')


if __name__ == "__main__":
    main()