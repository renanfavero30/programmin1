from pakudex import Pakudex

pakudex = Pakudex(capacity =2) # we dont need return to the pakuri class, we use this object to manipulate
species = "psygoose"
pakudex.add_pakuri2(species)

main_menu= ("""
Pakudex Main Menu\n
-----------------\n
1. List Pakuri\n
2. Show Pakuri\n
3. Add Pakuri\n
4. Evolve Pakuri\n
5. Sort Pakuri\n
6. Exit\n
What would you like to do?
""")

end_app = 0
print("Welcome to Pakudex: Tracker Extraordinaire!")
while end_app == 0:
    capacity_input = int(input("Enter max capacity of the Pakudex:"))
    while capacity_input >20 or capacity_input <1:
        print("Please enter a valid size.")
        capacity_input = input("Enter max capacity of the Pakudex:")
    print(f"The Pakudex can hold {capacity_input} species of Pakuri.")
    no_option = 0
    while no_option == 0:
        choice = int(input(main_menu))
        if choice is not in range(1, 6):
            no_option =0
        if choice == 1:
            Pakudex.get_species_array()
        if choice == 2:
            name_specie=(input("Enter the name of the species to display:"))
            if Pakudex.get_stats(name_specie) == None
                print("Error: No such Pakuri!")
                no_option == 0
            else:
                print(f"Species: {name_specie}")
                print("list_stats")
        if choice == 3:
            specie_to_add = input("Enter the name of the species to add:")
            if Pakudex.add_pakuri(specie_to_add) == True:
                print(f"Pakuri species {specie_to_add} successfully added!")
                no_option == 0
            elif Pakudex.add_pakuri(specie_to_add) == False:
                print("Error: Pakudex already contains this species!")
                break
            elif Pakudex.add_pakuri(specie_to_add) == "status":
                "Error: Pakudex is full!"
                break
        if choice == 4:
            name_evolve = input("Enter the name of the species to evolve:")
            if Pakudex.envolve_species(name_evolve) == False:
                print("Error: No such Pakuri!")
                no_option == 0
            else:
                print("{name_evolve} has evolved!")
                no_option == 0
        if choice == 5:
            Pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        if choice == 6:
            print("Thanks for using Pakudex! Bye!")
            break















