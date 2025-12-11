#Composition Type of Association
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus
    
class Employee:
    def __init__(self,name,age,salary):
        self.name = name 
        self.age = age
        self.obj_salary = salary

    def total_salary(self):
        return self.obj_salary.annual_salary()
    
salary = Salary(20000,10000)
emp = Employee("John",31,salary)
print("Your Annual Salary is: PKR/-",emp.total_salary())