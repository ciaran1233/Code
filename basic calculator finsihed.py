def add(x, y): 
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y 
def divide(x, y): 
    if y != 0: 
        return x / y 
    else:
        return "Cannot divide by zero"
    
    print ("select an operation")              #selecting a method 
    print("1,add")
    print("2,subtract")
    print("3,multiply")
    print("4,divide")
    
    choice = input ("choose a method from (1/2/3/4):") #the options of method linking with a number
    num1 = float (input("enter first number:")) #enter first number 
    num2 = float (input("enter second number:"))#enter second number
    
if choice == '1':#if option one it will add the 2 numbers
    print(add(num1,num2))
elif choice == '2': #it will  subtract the 2 numbers 
    print(subtract(num1,num2))
elif choice =='3':#it will  multiply the 2 numbers 
    print(multiply(num1,num2))
elif choice =='4':#it will  divide the 2 numbers 
    print(divide(num1,num2))
    
else: #if a invalid option is inputted it will print invalid
    print ("invalid input ")
    
calculator ()
complete = input("Thank you for using the calculator! Would you like to use it again? Y/N: ")         #this is where the system will thank the person for using the calulator and ask if they will ask if they want to use it again 
if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y":
        calculator()
elif complete == "No" or complete == "no" or complete == "n" or complete == "N":
        print("Thank you for using the Calculator, Goodbye!")
        quit()
else:
        print("ERROR: Unkown Input. Goodbye!")
        quit()
calculator()