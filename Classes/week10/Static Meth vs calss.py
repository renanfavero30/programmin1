# Composition
# has-a





@staticmethod #used as utility function, we canot change the the stances or atribute
def is_adult(age):
    return age > 18

# Using getattr ____________________________________________________________________

class Monster:
    def __init__(self, level =1, name ="Monster"):
        self.level = level
        self.name = NameError

    def increase_level(self, amaount):
        self.level += amaount



pikabu = Monster(2, "Pikabu")
print(getattr(pikabu, "level")) # same that pikabu.level 
print(pikabu.level)


# ____________________________________________________________________

class TeachingAssistant:
    # class attribute
    hourly_pay = 15

    def __init__(self, name, email= "admin@usl.edu", working_hours =0):
        self.name = name
        self.email = email
        self.working_hours = working_hours

    def run_discussion(self, working_hours):
        self.working_hours += working_hours

    def __str__(self):
        return f"{self.name} - {self.working_hours} is the result"

    def __eq__(self, other): #self = current object tan1 == ta2 (ta1 = self and ta2 = other)
        if isinstance(other, TeachingAssistant): # if other is a teachingassistant
            return self.email == other.email # true if is equal
        return False
    
    # def __lt__ (self, other): # tai<ta2 # SORTER
    #     if isinstance(other, TeachingAssistant):
    #         return self.name < other.name
        
    def __repr__(self): # for debuguing
        return f"{self.name} - {self.working_hours} is the result"
    
    def __add__(self, other):
        if isinstance(other, TeachingAssistant):
            return self.working_hours + other.working_hours
    
    


# ____________________________________________________________________

class Course:
    all_tas = [] #class attributes

    def __init__(self, name):
        self.name = name

    def add_tas(self, ta):
        self.all_tas # instance cs1
        self.all_tas.append(ta)



    @classmethod
    def average_working_hours(cls):
        #print(cls) #cls: Course
        return sum( ta.working_hours for ta in cls.all_tas) // len(cls.all_tas)

# ____________________________________________________________________

ta1 = TeachingAssistant("Andrew", "ap1@ufl.edu",69)
ta2 = TeachingAssistant("Karina", "ap1@ufl.edu", 2)

print(ta1.hourly_pay)

cs1 = Course("COP 3502 code")
cs1.add_tas(ta1)
cs1.add_tas(ta2)

print(Course.average_working_hours())



# The operator overloading __str__() method _________________________________________

print(ta1.name, ta1.email, ta1.working_hours)
#print(ta1) give us error
print(str(ta1))

# The __eq__ method


print(ta1==ta2) # if we dont' define the _eq__ method it compair the memory address | in this case compair emails

#  sort a list of integer ____________________________________________________________

a= [ 4, 5, 1, 3, 5]
a.sort()
a.sort(reverse = True)
print(a)

# sort the TAs
ta3 = TeachingAssistant("Shakira", "kv@ufl.edu",99)

tas = [ta1, ta2, ta3]
# tas.sort() - error we just know if they are equal or not, so we need create a criterial
# after include method lt__

# Approach 1 : define __lt__ method

# Approach 2 method __repr__ for debug

# Approach 3 method __ __

tas.sort(key= lambda ta: ta.working_hours) # each ta, sort by working_hours
print(f" approach 3{tas} this is the 1 TEST approach 3" )

tas.sort

for ta in tas: # we print just one per time, not in a list
    print(ta)

# after use the method __repr__
print(tas)


# include add method____________________________________________________________
""" 
def __add__(self, other):
    if isinstance(other, TeachingAssistant):
        return self.working_hours + other.working_hours
        """

hours = ta1 + ta2
print(hours)


