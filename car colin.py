class Car:
    def __init__(self, make, model, colour, price):
        self.make = make
        self.model = model
        self.colour = colour
        self.price = price

# Create two variables of the class Car and set the properties
mustang = Car("Ford", "Mustang 5.0 V8 GT Shadow Edition", "Shadow Black", 55000)
citroen = Car("Citroen", "C1 1.0 VTi Feel 5dr", "Red", 12000)

# Print the details of the cars
print(f"The {mustang.make} is a {mustang.colour} {mustang.model} and costs ${mustang.price}.")
print(f"The {citroen.make} is a {citroen.colour} {citroen.model} and costs ${citroen.price}.")
