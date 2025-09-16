#Example 1
#This asks for your name and prints hello there <your name>
yourname = input('What is your name?')
print ('Hello there ' + yourname) 

Example 2
#This adds the two numbers together and prints the answer 
n1 = float(input('Enter the first number.'))
n2 = float(input('Enter the second number.'))
print (n1 + n2) 

Example 3
#Converts meters entered to cm, km, inches, and prints the answers 
meters = float(input("Enter Meters"))
cm = meters * 100
km = meters / 1000
inches = meters * 39.37
print(str(meters) + " meters  = " + str(cm) + "cm, " + str(km) + "km") 

Example 4
#This multiplies the two numbers together and prints the answer
numb1 = float(input("Enter number 1:"))
numb2 = float(input("Enter number 2:"))
print(numb1 * numb2) 

Example 5
#'This defines two numbers, divides them and prints the answer
numb1 = 234
numb2 = 0
print (numb1 / numb2)

Example 6
# Python Program to show a for loop counting to an entered value
endValue = eval(input ("Enter the end number (between 5 and 12 "))
if endValue < 5 and endValue >= 12:
    for x in range(1, endValue):
        print (x)
    else:
        print("Entered value not in range")
        print("The end")

#the correct version
endValue = int(input ("Enter the end number between 5 and 12 "))
if endValue >=5 and endValue <=12:
    for x in range(1,endValue +1 ):
     print (x)
else:
 print("Entered value not in range")
print("The end")