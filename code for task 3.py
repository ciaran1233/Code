# def calculate_square_root():

#   num = int(input("Enter a number to find the square root: "))

#   result = num ** 0.5

#   print("The square root of", num, "is", result)



# def read_file():

#   file = open("data.txt", "r")

#   content = file.read()

#   print("File Content:\n", content)



# def divide_numbers():

#   num1 = int(input("Enter the numerator: "))

#   num2 = int(input("Enter the denominator: "))

#   result = num1 / num2

#   print("The result of division is:", result)



# # Main program

# calculate_square_root()

# read_file()

# divide_numbers()



import logging

def read_file():
    try:
        with open("data.txt", "r") as file:  # Automatically closes the file
            content = file.read()
            if content.strip():  # Check if the file is not empty
                print(content)
            else:
                print("The file is empty.")
    except FileNotFoundError:
        logging.error("File 'data.txt' not found.")
    except PermissionError:
        logging.error("Permission denied when trying to read 'data.txt'.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def divide_numbers():
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        
        result = num1 / num2
        print(f"The result is {result}")
    
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except ZeroDivisionError:
        logging.error("Error: Denominator cannot be zero.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Main program
read_file()
divide_numbers()
