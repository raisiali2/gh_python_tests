# class Car:
#     #  class constructor method to initialize instances
#     def __init__(self, make, model, year):
#         self.make = make # instance variable
#         self.model = model # instance variable 
#         self.year = year # instance variable

#     # instance method to describe the car
#     def description(self):
#         return f"{self.year} {self.make} {self.model}"
    
#     # instance method to simulate driving the car
#     def drive(self):
#         return f"the {self.model} is now driving."
    
# # creating instance of the Car
# car1 = Car("toyota", "corolla", 2020)
# car2 = Car("ford", "mustang", 2022)

# # car1 and car2 are both objects and instances of the Car class.
# # the distinction is in the relationship: each is an object in the general sense.
# # and each is specifically an instance of the Car class.

# # using methods associated with these instances
# print(car1.description()) # calls the description method on the car1 instance
# print(car2.drive()) # calss the drive method on the car2 instance


class Person:
    # class attribute
    species = "canis familiaris"

    # initializer / instance attribute
    def __init__(self, fname, lname):
    # assign values to object properties
    # __init__() is called automatically every time the class is being used to create a new object
    # self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
        self.firstname = fname
        self.lastname = lname

    # method
    def description(self):
        return f"{self.firstname} and {self.lastname}"

    def speak(self, language):
        self.language = language
        return f"his firstname is {self.firstname} and his lastname is {self.lastname} and he speaks {self.language}"
    
person1 = Person("ali", "raisi")
# print(person1.description())
print(person1.speak("french")) 
# print(person1.firstname)
# print(person1.lastname)
# print(person1.language)     
