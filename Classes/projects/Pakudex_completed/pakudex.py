# Import the Pakuri class
from pakuri import Pakuri


# Define the Pakudex class
class Pakudex:
    # Initialize the Pakudex with a default capacity of 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuris = []

    # Return the current number of Pakuri in the Pakudex
    def get_size(self):
        return len(self.pakuris)

    # Return the maximum capacity of the Pakudex
    def get_capacity(self):
        return self.capacity

    # Return an array of Pakuri species currently in the Pakudex
    def get_species_array(self):
        if self.get_size() == 0:
            return None

        list_species = []
        for pakuri in self.pakuris:
            list_species.append(pakuri.get_species())
        return list_species

    # Return a list of stats (attack, defense, speed) for a given species
    def get_stats(self, species):
        list_stats = []
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                list_stats.append(pakuri.get_attack())
                list_stats.append(pakuri.get_defense())
                list_stats.append(pakuri.get_speed())
                return list_stats
        return None

    # Sort the Pakuri in the Pakudex alphabetically by species name
    def sort_pakuri(self):
        self.pakuris.sort(key=lambda pakuri: pakuri.get_species())

    # Add a new Pakuri to the Pakudex if it doesn't already exist and if there is room
    def add_pakuri(self, species):
        if self.get_size() == self.get_capacity():
            return False

        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                return False

        self.pakuris.append(Pakuri(species))
        return True

    # Evolve a Pakuri of the given species if it exists in the Pakudex
    def evolve_species(self, species):
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
