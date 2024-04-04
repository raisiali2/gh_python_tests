# inherits allow to define a class that inherits all the methods and properties from another class
# parent class: is base class
# child class: inherit from another class, is called derived class

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass
# this child class inherits the properties and method from base class

# create object of the class and the execute the printname method

# p1 = Person("ali","raisi")
# p1.printname()

# use Student class to create an object

# p2 = Student("james","trump")
# p2.printname()

#=============== add __init__() function to the child class instead of pass
# when we add __init__(), the child class no more iherit from parent class
# the child __init__() overrides the inheritance of the parent's __init__() function.

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
       

# p2 = Student("james","trump")
# p2.printname()


#================== to keep inheritance of parent's __init__(), add a call to the parent's __init__()===============

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
       
# p3 = Student("mike","olsen")
# p3.printname()

# we have successfully added __init__() and kept inheritance of the parent class, and we are ready
#==================================================================================================
# to add functionality in the __init__()
# to add functionality to child class use super() function

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
       
# p4 = Student("mike","olsen")
# p4.printname()

# super() function make the child class inherit from properties and methods of the parent class


#====================add properties==============================================================


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019
       
# p5 = Student("mike","olsen")
# print(p5.graduationyear)
#============================================================================================
# now add the 2019 as variable and pass into the student class when creating student objects.
# to do that add another parameter in the __init__()

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
       
# p5 = Student("mike","olsen", 2019)
# print(p5.graduationyear)


#====================add methods==========================================================

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)
       
p6 = Student("mike","olsen", 2019)
p6.welcome()
