"""
The Dragon class must be derived from the Cow class and must make all of its methods available. In addition,
Dragon must provide the following methods:

"""
from cow import Cow

""" 
__init__(self, name, image)
Constructor; creates a new Dragon object with the given name and image.
can_breathe_fire()
This method should exist in every Dragon class. For the default Dragon type, it should always return True.
"""

class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name) # same that super().__init__(name)
        self.image = image

    def can_breathe_fire(self):
        if Cow.get_name() == "dragon":
            return True
