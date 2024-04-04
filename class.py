class Car:
    #  class constructor method to initialize instances
    def __init__(self, make, model, year):
        self.make = make # instance variable
        self.model = model # instance variable 
        self.year = year # instance variable

    # instance method to describe the car
    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
    # instance method to simulate driving the car
    def drive(self):
        return f"the {self.model} is now driving."
    
# creating instance of the Car
car1 = Car("toyota", "corolla", 2020)
car2 = Car("ford", "mustang", 2022)

# car1 and car2 are both objects and instances of the Car class.
# the distinction is in the relationship: each is an object in the general sense.
# and each is specifically an instance of the Car class.

# using methods associated with these instances
print(car1.description()) # calls the description method on the car1 instance
print(car2.drive()) # calss the drive method on the car2 instance
      
