#Reference Based Aggregation Method Code
class Teacher:
    def __init__(self,name):
        self.name = name

        #Teacher does not create Student object, only holds reference
        self.students = []

    def add_Students(self,student):
        self.students.append(student) #teacher only holds reference to student object

    
class Student:
    def __init__(self,name):
        self.name = name