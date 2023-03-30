class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuris = []  # add one pakury per time (append 1 per time)

    def get_size(self):
        return len(self.pakuris)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if self.pakuris == []:
            return None
        else:
            return str(self.pakuris)

    def get_stats(self, species):
        pass

    def sort_pakuri(self):
        self.pakuris.sort()

    def add_pakurit(self, species):
        self.pakuris
        self.pakuris.append(species)

    def envolve_species(self, species):
        pass
        def add_tas(self, ta):
            self.all_tas  # instance cs1
            self.all_tas.append(ta)

