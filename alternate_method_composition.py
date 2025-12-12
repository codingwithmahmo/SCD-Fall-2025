#Constructor-Based Composition Alternative Method Code
class Student:
    def __init__(self,name):
        self.name = name

        #Constructor based Composition
        #Student creates and owns the profile Object
        self.profile = Profile(self.name)
        #if the student is deleted, profile will also be deleted

class Profile:
    def __init__(self,student_name):
        self.student_name = student_name