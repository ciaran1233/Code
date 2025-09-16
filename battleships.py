board = [[' ', ' ', '8', ' '],
         [' ', ' ', '8', ' '],
         [' ', ' ', '8', ' '],
         [' ', ' ', ' ', ' ']]
boardHits = [[' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ']]


print("Welcome to the Battleship game")
print("Sink the Battleship in 10 goes or less")

# Initialize variables
hits = 0
goes = 0

running = True

while running:
    # Display the board
    print("  1 2 3 4")
    for y in range(4):
        print(y + 1, end=' ')
        for x in range(4):
            print(boardHits[y][x], end=' ')
        print()

    # Get user input
    try:
        x_guess = int(input("Enter the X coordinate (1-4): ")) - 1
        y_guess = int(input("Enter the Y coordinate (1-4): ")) - 1
        
        if x_guess not in range(4) or y_guess not in range(4):
            print("Invalid coordinates, please enter numbers between 1 and 4.")
            continue
        
    except ValueError:
        print("Please enter valid numbers.")
        continue
    
    goes += 1
    print(f"Go number: {goes}")

    if board[y_guess][x_guess] == '8':  # Assuming '8' represents the battleship
        print("Hit!")
        boardHits[y_guess][x_guess] = '#'
        hits += 1
    else:
        print("Miss!")
        boardHits[y_guess][x_guess] = '-'
    
    if hits == 3:  # Assuming there is only one battleship to sink
        print("Congratulations! You've sunk the battleship!")
        running = False

    if goes >= 10 and hits < 1:  # Updated condition for game over
        print("Game over! You've used all your goes.")
        running = False
        
  