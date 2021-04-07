
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not(char.issuperset(lname) and char.issuperset(fname) and char.issuperset(major)):
           raise ValueError
        
        if not (isinstance(gpa, float) and 0.0 <= gpa <=4.0):
           raise ValueError
        
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
