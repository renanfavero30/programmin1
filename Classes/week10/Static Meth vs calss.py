# Composition
# has-a

class TeachingAssistant:
    # class attribute
    hourly_pay = 15

    def __init__(self, name, email= "admin@usl.edu", working_hours =0):
        self.name = name
        self.email = email
        self.working_hours = working_hours

    def run_discussion(self, working_hours):
        self.working_hours += working_hours

class Course:
    all_tas = [] #class attributes

    def __init__(self, name):
        self.name = name

    def add_tas(self, ta):
        self.all_tas # instance cs1
        self.all_tas.append(ta)


    @classmethod
    def average_working_hours(cls):
        print(cls) #cls: Course
        return sum( ta.working_hours for ta in cls.all_tas) // len(cls.all_tas)


ta1 = TeachingAssistant("Andrew", "ap1@ufl.edu")
ta2 = TeachingAssistant("Karina", "kan@ufl.edu", 2)

print(ta1.hourly_pay)

cs1 = Course("COP 3502 code")
cs1.add_tas(ta1)
cs1.add_tas(ta2)

print(Course.average_working_hours())

    @staticmethod #used as utility function, we canot change the the stances or atribute
    def is_adult(age)
        return age > 18


