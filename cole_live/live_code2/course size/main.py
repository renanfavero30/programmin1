class Student:
    def __init__(self, first, last, gpa):
        self.name = first
        self.last = last
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, new_gpa):
        self.gpa = new_gpa


class Course:
    def __init__(self ):
        self.roster = []  # later we will add students in the roster

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)


if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Bendel', 3.6))
    course.add_student(Student('Johnny', 'Moin', 2.9))

    print('Course size:',course.course_size())