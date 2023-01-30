# LAB 2 - Renan Favero
import math as m
"""
Sample Output
Example #1
⎯⎯⎯⎯⎯⎯⎯
Enter first operand: 2.25
Enter second operand: -1.5

Calculator Menu
---------------
1. Addition
2. Subtraction
3. Multiplication
4. Division

Which operation do you want to perform? 4

The result of the operation is -1.5. Goodbye!
"""
# Input the nros for the variables 1 and 2
nro1 = float(input("Enter first operand: "))
nro2 = float(input("Enter second operand: "))

# Insert the menu
option = int(input(f"Calculator Menu \n"
                   f" --------------- \n"
                   f" 1. Addition \n"
                   f" 2. Subtraction \n"
                   f" 3. Multiplication \n"
                   f" 4. Division \n"
                   f" \n"
                   f" Which operation do you want to perform? "))

# Calculate the result
if option == 1:
    nr3= nro1 + nro2
elif option == 2:
    nr3 = nro1 - nro2
elif option == 3:
    nr3 = nro1 * nro2
else:
    nr3 = nro1 / nro2

# Output the result
print(f'The result of the operation is {nr3}. Goodbye!')




