# Define the constant PASSWORD
PASSWORD = "LetMeIn"

# Function to check password
def check_password():
    while True:
        user_password = input("Enter your password: ")
        if user_password == PASSWORD:
            print("Login successful")
            break
        else:
            print("Incorrect password")

# Main program to display a welcome message and check password
def main():
    print("Welcome! Please log in to continue.")
    check_password()

# Run the main program
if __name__ == "__main__":
    main()