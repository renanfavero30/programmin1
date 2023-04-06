from Classes.projects.Project_3_Pakudex.pakuri import Pakuri

# Create the class pakudex
class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity # default value is 20
        self.pakuris = []  # add one pakury per time (append 1 per time) | store a list of pakuri objects
        self.size = 0 # keep track of the # concrete pakuri in pakudex

    def get_size(self):
        return len(self.pakuris)

    def get_capacity(self):
        return self.capacity

    def add_pakuri2(self, species):
    # 1. Check duplicates - > return False
        if species in self.get_species_array():
            print("Specie duplicated")
    #2. When the list is full = False
        if self.capacity == self.size
            print("Error: Pakudex is full!")
    #3. Add a new pakuri object into the list
        else:
            self.pakuri.append(Pakuri(species)) #create a Pakuri
            self.size += 1
            return True

    def get_species_array(self):
        if self.get_size() == 0:
            return None
        else:
            list_species = []
            for pakuri in self.pakuris:
                list_species.append(pakuri.get_species())
            return list_species



'''
Action 1:
Hau's Pakudex = new Pakudex(5)

Result
HauPakudex {
    self.capacity = 5
    self.pakuri = []
    
}

Action 2: Add Pakuri "dog" to HauPakuDex

Result 2
HauPakudex{
    self.capacity = 5
    self.pakuri = [
        dog {
            species = "dog"
            attack = 10
            defense = 20
            speed = 30
        }
    ]
    
Action 3: Add Pakuri "elephant" to HauPakuDex

Result 3
HauPakudex{
    self.capacity = 5
    self.pakuri = [
        dog {
            species = "dog"
            attack = 10
            defense = 20
            speed = 30
        },
        elephant {
            species = "elephant"
            attack = 12
            defense = 24
            speed = 36
        }
    ]
'''
    def get_stats(self, species):
        list_stats = []
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                list_stats.append(pakuri.get_attack())
                list_stats.append(pakuri.get_defense())
                list_stats.append(pakuri.get_speed())
                return list_stats
        return None

    def sort_pakuri(self):
        self.pakuris.sort(key= lambda pakuri:pakuri.get_species())
        #orig_list.sort(key=lambda x: x.count, reverse=True)

        '''
        self.myStrings = ['hi', 'bye', 'dog', 'apple']
        
        self.myStrings.sort()
        
        Point {
            x : int
            y : int
        }
        self.points = [ new Point(1,2), new Point(3,4), new Point(6,-2)]
        //( 6,-2), (1,2) (3,4)
        
        self.points.sort()
        
        self.points.sort(key:lambda point: point.y)
        
        '''

    def add_pakuri(self, species): # species is a string object
        # When can you add?
        # 1. if you have capacity
        # 2. If the species does not exist in your pakudex

        list_has_species = False

        # determine if my list of pakuris has the species
        # self.pakuris -> a list of pakuris
        # self.capacity -> number
        # species -> string

        '[ pakuri(dog), pakuri(elephant)]'

       #  pakuri in self.pakuris # self.pakuri is the list, species is the pakuri (pakuri(dog)) in first iteration
        # pakuri(elephant) on second iteration
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                list_has_species = True


        # for each pakuri in pakuris
        # get the species of the pakuri
        # check if species of pakuri is equal to species in argument to function
        # if equal, set list_has_species to true and break from loop
        # else continue with loop
        if len(self.pakuris) >= self.capacity:
            status = "full"
            return status

        if len(self.pakuris) < self.capacity and list_has_species == False  :
            self.pakuris.append(Pakuri(species))
            return True
        return False


        # How do we trun a string like 'dog' to a pakuri object?
         #Pakuri(species)
        # self.pakuri is a list of Pakuri objects
        # [ dog {}, elephant {}, 'cat']

    def envolve_species(self, species):
        list_has_species = False
        for pakuri in self.pakuris:
            if pakuri.get_species() == species:
                list_has_species = False


        # at this line you have a variable that tells you if your list contains the species or not
        # variable is list_has_species


        # if we have species in the list
        # we need to get the pakuri and evolve it
        # return true
        if list_has_species == True:
            for pakuri in self.pakuris:
                if pakuri.get_species() == species:
                    pakuri.evolve()
                    return True
        return False
            # you have access to self.pakuris, self.capacity, species
            #self.pakuris
            # get pakuri
            # .evolve()

        #if we do not have the species in the list
        # return false
