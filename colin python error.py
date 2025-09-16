print("Welcome to Python Error Code - project pine tree")

# Subroutine to print a number of characters on the same line
def PrintChars(number_of, chars):
    for i in range(number_of):
        print(chars, end="")

# Main program
print("Draw a pine tree")
size = int(input("Enter a size between 3 and 15: "))

# Validate the input size
if size < 3 or size > 15:
    print("Size must be between 3 and 15.")
else:
    pos = size + 10  # Adjusting position for centering the tree

    # This part draws the main tree using Xs
    for i in range(size):
        PrintChars(pos, " ")        # Print spaces for centering
        PrintChars(i * 2 + 1, "X")  # Print the Xs for the tree
        print()  # Move to the next line
        pos -= 1  # Decrease position for the next line

    # This part draws the trunk using the letter I
    trunk_height = size // 3
    for i in range(trunk_height):
        PrintChars(size + 10, " ")  # Centering the trunk
        PrintChars(1, "I")           # Draw the trunk
        print()  # Move to the next line