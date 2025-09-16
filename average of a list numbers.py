def calculate_average(numbers):
    try:
        # Check if the input is a valid list of numbers
        if not isinstance(numbers, list):
            return "Error: Input is not a valid list."
        
        # If the list is empty, return an error message
        if not numbers:
            return "Error: The list is empty. Please provide a list with at least one number."
        
        # Ensure all elements in the list are numbers (int or float)
        valid_numbers = [num for num in numbers if isinstance(num, (int, float))]
        
        # If no valid numbers are present after filtering, return an error message
        if not valid_numbers:
            return "Error: The list contains no valid numbers. Please provide a list of numbers."
        
        # Calculate the average
        average = sum(valid_numbers) / len(valid_numbers)
        return average
    
    except TypeError:
        return "Error: The input is not a valid list of numbers."
    except Exception as e:
        return f"Unexpected error: {e}"

def get_user_input():
    while True:
        try:
            # Take a string input from the user (comma-separated numbers)
            user_input = input("Please enter a list of numbers separated by commas (e.g., 1, 2, 3, 4): ")
            
            # Convert the input string into a list of numbers
            number_list = [float(item.strip()) for item in user_input.split(",")]
            
            # Call calculate_average with the list of numbers
            result = calculate_average(number_list)
            
            # Print the result and exit if successful
            print(f"Average: {result}")
            break
        
        except ValueError:
            print("Error: Invalid input. Please enter a list of numbers separated by commas.")

# Call the function to get user input
get_user_input()