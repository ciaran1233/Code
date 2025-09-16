class Car:
    def __init__(self, make, model, colour, price):
        self.make = make
        self.model = model
        self.colour = colour
        self.price = price

    def printDetails(self):
        print(f"The {self.make} is a {self.colour} {self.model} and costs ${self.price}.")

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

    def calculateTimeToAffordCar(self, car_price):
        # Get the employee's wage
        wage = self.getWage()
        # Calculate how many years it will take to afford the car
        time_in_years = car_price / wage
        return time_in_years

# Create car objects
mustang = Car("Ford", "Mustang 5.0 V8 GT Shadow Edition", "Shadow Black", 55000)
citroen = Car("Citroen", "C1 1.0 VTi Feel 5dr", "Red", 12000)

# Create an employee object
employee1 = Employee(30000, 10, 20)

# Calculate and print the time to afford each car
time_to_afford_mustang = employee1.calculateTimeToAffordCar(mustang.price)
time_to_afford_citroen = employee1.calculateTimeToAffordCar(citroen.price)

# Output results
mustang.printDetails()
print(f"It will take approximately {time_to_afford_mustang:.2f} years to afford the Mustang.")

citroen.printDetails()
print(f"It will take approximately {time_to_afford_citroen:.2f} years to afford the Citroen.")
