# Import the Pakudex class from the pakudex module
from pakudex import Pakudex

# Define the main menu string for user input
main_menu = """
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit

What would you like to do?
"""

# Print a welcome message
print("Welcome to Pakudex: Tracker Extraordinaire!")

# Get the user input for the maximum capacity of the Pakudex
capacity_input = int(input("Enter max capacity of the Pakudex: "))
while capacity_input < 1:
    print("Please enter a valid size.")
    capacity_input = int(input("Enter max capacity of the Pakudex: "))
print(f"The Pakudex can hold {capacity_input} species of Pakuri.")

# Create a new Pakudex object with the given capacity
pakudex = Pakudex(capacity=capacity_input)

# Initialize a flag to control the program loop
exit_option = 0

# Main program loop
while not exit_option:
    # Get the user's menu choice
    choice = int(input(main_menu))

    # Validate the menu choice
    if choice not in range(1, 7):
        print("Unrecognized menu option.")
        continue

    # Execute the appropriate action based on the menu choice
    if choice == 1:
        list_pakuri = pakudex.get_species_array()
        if not list_pakuri:
            print("No Pakuri in Pakudex yet!")
        else:
            print("Pakuri In Pakudex:")
            for index, value in enumerate(list_pakuri):
                print(f"{index + 1}. {value}")
        continue

    if choice == 2:
        name_specie = input("Enter the name of the species to display: ")
        stats = pakudex.get_stats(name_specie)
        if not stats:
            print("Error: No such Pakuri!")
        else:
            print()
            print(f"Species: {name_specie}")
            print(f"Attack: {stats[0]}")
            print(f"Defense: {stats[1]}")
            print(f"Speed: {stats[2]}")
        continue

    if choice == 3:
        if pakudex.get_size() == pakudex.get_capacity():
            print("Error: Pakudex is full!")
            continue

        specie_to_add = input("Enter the name of the species to add: ")
        if pakudex.add_pakuri(specie_to_add) == True:
            print(f"Pakuri species {specie_to_add} successfully added!")
        else:
            print("Error: Pakudex already contains this species!")
            continue

    if choice == 4:
        name_evolve = input("Enter the name of the species to evolve: ")
        if pakudex.evolve_species(name_evolve) == False:
            print("Error: No such Pakuri!")
        else:
            print(f"{name_evolve} has evolved!")
        continue

    if choice == 5:
        pakudex.sort_pakuri()
        print("Pakuri have been sorted!")
        continue

    if choice == 6:
        exit_option = True
        print("Thanks for using Pakudex! Bye!")
