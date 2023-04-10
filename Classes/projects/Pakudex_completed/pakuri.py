# Define the Pakuri class
class Pakuri:
    # Initialize the Pakuri with the given species and calculate its stats based on the species name length
    def __init__(self, species):
        self.__species = species
        self.__attack = (len(species) * 7) + 9
        self.__defense = (len(species) * 5) + 17
        self.__speed = (len(species) * 6) + 13

    # Return the species name of the Pakuri
    def get_species(self):
        return self.__species

    # Set the species name of the Pakuri
    def set_species(self, new_species):
        self.__species = new_species

    # Return the attack stat of the Pakuri
    def get_attack(self):
        return self.__attack

    # Return the defense stat of the Pakuri
    def get_defense(self):
        return self.__defense

    # Return the speed stat of the Pakuri
    def get_speed(self):
        return self.__speed

    # Set the attack stat of the Pakuri
    def set_attack(self, new_attack):
        self.__attack = new_attack

    # Evolve the Pakuri by updating its stats
    def evolve(self):
        self.__attack = self.__attack * 2
        self.__defense = self.__defense * 4
        self.__speed = self.__speed * 3
