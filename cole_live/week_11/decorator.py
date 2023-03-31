

@property #getter
def fullname(self): # it is an atribute, not a method
    return f"({self.firts} {self.last})"

@fullname.setter #setter
def fullname(self, name):
    self.firts, self.last = name.split()

emp = Employee ("Tom", "Smith")

