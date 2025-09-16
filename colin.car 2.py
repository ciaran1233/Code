class Car:
    def __init__(self, make, model, colour, price):
        self.make = make
        self.model = model
        self.colour = colour
        self.price = price

    def printDetails(self):
        print(f"The {self.make} is a {self.colour} {self.model} and costs ${self.price}.")

# Create two variables of the class Car and set the properties
mustang = Car("Ford", "Mustang 5.0 V8 GT Shadow Edition", "Shadow Black", 55000)
citroen = Car("Citroen", "C1 1.0 VTi Feel 5dr", "Red", 12000)

# Print the details of the cars using the printDetails method

mustang.printDetails()
citroen.printDetails()


# Employee class with getWage method
class Employee:
    def __init__(self, base_salary, overtime_hours, overtime_rate):
        self.base_salary = base_salary
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def getWage(self):
        # Ensure overtime hours and rate are non-negative
        if self.overtime_hours < 0 or self.overtime_rate < 0:
            raise ValueError("Overtime hours and rate must be non-negative.")
        return self.base_salary + (self.overtime_hours * self.overtime_rate)

# Create an Employee object
employee1 = Employee(30000, 10, 20)

# Calculate and print the wage
wage = employee1.getWage()
print(f"The wage for employee1 is ${wage}.")

