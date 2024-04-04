class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):

        print (f"first name: {self.fname} and last name: {self.lname}")

class Student(Person):
    def __init__(self, fname, lname, year):
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduation_year = year

    def Welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)


class Employee(Person):
    pass


# x = Person("ali", "raisi")
# x.printname()
# x = Student("ali", "raisi")
# x.printname()
# x = Employee("james","jan")
# x.printname()
# x = Student("sakhi", "shokouh", 2019)
# print(x.graduation_year)

x = Student("jan", "trump", 2022)
x.Welcome()

