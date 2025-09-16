import math
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_square_root(value):
    # Input validation: Check if the input is of the correct type and non-negative.
    if not isinstance(value, (int, float)):
        logging.error("Invalid input type. Expected a number.")
        raise TypeError("Input must be an integer or float.")
    
    if value < 0:
        logging.error("Invalid input. Negative numbers do not have real square roots.")
        raise ValueError("Input must be a non-negative number.")
    
    # Assertion to ensure input is validated correctly
    assert isinstance(value, (int, float)) and value >= 0, "Precondition check failed: input must be non-negative integer or float."
    
    try:
        # Calculate square root
        result = math.sqrt(value)
        
        # Post-condition assertion: Result should always be a non-negative number.
        assert result >= 0, "Postcondition check failed: result should be non-negative."
        
        logging.info(f"Square root of {value} is {result}")
        return result
    
    except ValueError as e:
        # Error handling: Log and raise an exception if something goes wrong
        logging.error("Error calculating square root: " + str(e))
        raise
    
    except Exception as e:
        # Catch-all for unforeseen exceptions
        logging.critical("Unexpected error: " + str(e))
        raise

def get_user_input():
    while True:
        user_input = input("Please enter a non-negative number to calculate its square root: ")
        
        try:
            # Convert the input to a float (this works for both integers and floating-point numbers)
            value = float(user_input)
            
            # Call the function to calculate the square root
            return calculate_square_root(value)
        
        except ValueError:
            # If conversion to float fails, print a message and ask again
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            # Catch any other unforeseen exceptions
            print(f"Error: {e}")

# Example usage: Get user input and calculate the square root
get_user_input()