
"""
Private variable = just accessible inside the class
Public variable = accessible by anyone from anywhere
Protected variable = accessible by a subclass or child class

In Python all variables are public, and add the __ is a way to signal others users program that this is a private variable
that should not be touch but it doesnt prevent to be touched.
"""

class Pakuri:
    # antPakuri = new Pakuri('ant')
    def __int__(self, species):
        self.__species = species
        self.__attack = (len(species) * 7) + 9
        self.__defense = (len(species) * 5) + 17
        self.__speed = (len(species) * 6) + 13

    # getters and setters
    # getters: retreive the values of an attribute
    
    def get_species(self):
        return self.__species

    def get_attack(self):
        return self.__attack

    def get_defense(self):
        return self.__defense

    def get_speed(self):
        return self.__speed

    def set_attack(self, new_attack):
        self.__attack = new_attack

    def evolve(self):
        self.__attack = self.__attack * 2
        self.__defense = self.__defense * 4
        self.__speed = self.__speed * 3


"""
Next steps:
Pakudex class
Pakuri progam.py

"""