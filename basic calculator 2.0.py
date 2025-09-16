def add (x,y):
    return x+y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x *y 
def divide (x,y):
    if y != 0:
        return x /y
    else:
        return "cannot divide by zero"
    
    
print("select an operation:")
print("1,add")
print("2,subtract")
print("3,multiply")
print("4,divide")

choice = input ("choose a method from (1/2/3/4):")
num1 = float (input("enter first number:"))
num2 = float (input("enter second number:"))


if choice =='1':
    print (add (num1,num2))
elif choice == '2' :
    print (subtract (num1,num2))
elif choice == '3' :    
      print (multiply (num1,num2))
elif choice == '4':
    print(divide(num1,num2))

else:
    print ("invalid input ")
    
claculator ()
complete = input("Thank you for using the calculator! Would you like to use it again? Y/N: ")
if complete == "Yes" or complete == "yes" or complete == "y" or complete == "Y":
        calculator()
elif complete == "No" or complete == "no" or complete == "n" or complete == "N":
        print("Thank you for using the Calculator, Goodbye!")
        quit()
else:
        print("ERROR: Unkown Input. Goodbye!")
        quit()
calculator()