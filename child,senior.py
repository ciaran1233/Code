def age_category(age):
    if age < 0: 
        return "Invalid age" 
    elif age <= 12: 
        return "You are a child." 
    elif age <= 19: 
        return "You are a teenager." 
    elif age <= 64: 
        return "You are an adult." 
    elif age<70:
        return "You are a senior." 
try:
    age = int(input("Please enter your age: ")) 
    print(age_category(age)) 
except ValueError: 
    print("Please enter a valid number.")
     
if user_input.isdigit():
    age  = int(user_input )
    print(age_category(age))
else:
    print("Please enter a valid number.")