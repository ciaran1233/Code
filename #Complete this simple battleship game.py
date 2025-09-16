#Complete this simple battleship game
board = [[' ', ' ', '8', ' '],
         [' ', ' ', '8', ' '],
         [' ', ' ', '8', ' '],
         [' ', ' ', ' ', ' ']]
boardHits = [[' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ']]

#Initial program announcement
print("Welcome to the Battleship game")
print("Sink the Battleship in 10 goes or less")

#Set initial variables
hits = 0
goes = 0
running = True

while running:
    #Output the board hits with axis using the boardHits array as data (for loops needed here)
   print ("1 2 3 4")
   for y in range (4):
        print (y+1,end = '')
        for x in range (4):
            print(board[y][x],end = "")
        print()
    #Ask the user for x and y coordinates using data validation
x = int(input("enter the x co-ordinate of the guess")) -1 
y = int(input("enter the y  co-ordinate of the guess")) - 1
    #Increment goes and let the user know how many goes they have had
    
    #Record the go coordinates in the boardHits array (# symbol at the coordinate for hit, - for miss)
    
    #If a hit, add 1 to hits

    #If ship sunk (hits = 3), annouce game won and the game ends (running = False)
    
running = False # tempoary code to stop the while loop repeating - delete this when you need to

    #else if they are out of goes, annouce game lost and the game ends (running = False)


#Note, you might find it useful to output the board array too until you have everything working

#Once you get the game working, and if time allows consider enhancements to the game.
#Possible enhancements to the game could be:
# If the game lost, show the user where the ship(s) were
# A larger board
# More ships to sink
# Random initial positions of ships (this is advanced)