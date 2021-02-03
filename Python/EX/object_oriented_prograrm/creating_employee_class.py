# creating instance object of employee class
class Employee:
    empCout = 0

    def __init__(self, name, selary):
        self.name = name
        self.selary = selary
        Employee.empCout += 1

    def displayCount(self):
        print("Total Employee = %d" % Employee.empCout)

    def displayEmployee(self):
        print("Name : ", self.name, "Selary", self.selary)


# creating instance object
Employee_1 = Employee("John", 25000)
Employee_2 = Employee("lisa", 20000)

Employee_1.displayEmployee()
Employee_2.displayEmployee()

Employee_1.displayCount()

