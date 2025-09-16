def main():
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
     while True:
        try:
            interest_rate = int(input("Please enter an interest rate: "))
            if interest_rate > 10:
                confirm = input("Entered interest rate is greater than 10%. Are you sure? (y/n): ")
                if confirm =="y":
                    break
            elif 0 <= interest_rate < 10:
                break
        except ValueError:
            print("Entered value is not a number! ") 

