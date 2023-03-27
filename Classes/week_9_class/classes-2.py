class TeachingAssistant:
    # class attribute
    hourly_pay = 15

    def __init__(self, name, email= "admin@usl.edu", working_hours =0):
        self.name = name
        self.email = email
        self.working_hours = working_hours

    def __str__(self):
        return f" example = {self.name} - {self.email} - {self.working_hours} - {TeachingAssistant.hourly_pay} or {self.hourly_pay}"

kevin = TeachingAssistant("Kevin", "kevinzhang@ufl.edu", 10)
kevin2 = TeachingAssistant("Kevin")

# to access the hourly pay
print(TeachingAssistant.hourly_pay)

andrew = TeachingAssistant( "Andrew", "andreq@ufl.edu", 6)

print(kevin)
print(kevin2)

print(andrew.hourly_pay)

# increase the salary of andrew
andrew.hourly_pay = 30
print(TeachingAssistant.hourly_pay) # return 15, because the default value is 15
print(kevin.hourly_pay)
print(andrew.hourly_pay) # it should change to 30
