"""
The IceDragon class must be derived from the Dragon class and must make all of its methods available
"""
from cow import Cow
from dragon import Dragon

"""
__init__(self, name, image)
Constructor; creates a new IceDragon object with the given name and image.
can_breathe_fire()
For the IceDragon type, this method should always return False.
"""


class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image) #How do I know what arguments include here?

    def can_breathe_fire(self):
        return False