def main():

def getname():
name = input("what is your name?:")
return name
 
while True:
        try:
            years_left = int(input("Please enter the number of years left until retirement (1-65): "))
        except ValueError:
            print ("Entered value is not a number! Please enter a number 1-65.")
        except KeyboardInterrupt:
            print("Command Error! Please enter a number 1-65.")
        else:
            if 1 <= years_left < 65:
                break
            else:
                print("Entered value is not in the range 1-65.")

