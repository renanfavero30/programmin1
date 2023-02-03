input_plz = -1
while input_plz != 0:
    input_plz = int(input("Enter a positive integer:"))

    if input_plz < 0:
        print("Error: negative number. Terminating")
        break  # skip everything after the break inside the while loop

    print(f'You entered {input_plz}')
