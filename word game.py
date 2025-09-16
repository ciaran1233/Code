import random
import time

# List of sample categories and words
categories = {
    'animals': ['elephant', 'tiger', 'lion', 'giraffe', 'zebra', 'cat', 'dog'],
    'fruits': ['apple', 'banana', 'grape', 'orange', 'kiwi', 'peach'],
    'countries': ['australia', 'brazil', 'canada', 'denmark', 'egypt', 'finland']
}

# Function to start the game
def start_game():
    print("Welcome to Word Chain Challenge!")
    print("Choose a category:")
    print("1. Animals")
    print("2. Fruits")
    print("3. Countries")

    category_choice = int(input("Enter your choice (1/2/3): "))

    if category_choice == 1:
        category = 'animals'
    elif category_choice == 2:
        category = 'fruits'
    elif category_choice == 3:
        category = 'countries'
    else:
        print("Invalid choice. Starting with Animals by default.")
        category = 'animals'

    words = categories[category]
    play_round(words)

# Function to play a round
def play_round(words):
    print(f"\nYou are playing in the {category} category.")
    print("Let's start the word chain!\n")
    time.sleep(1)

    # Randomly choose the first word
    current_word = random.choice(words)
    print(f"Starting word: {current_word.capitalize()}")

    used_words = [current_word]
    player_turn = True

    while True:
        if player_turn:
            # Player's turn to give a word
            print(f"\nThe last word is: {current_word.capitalize()}")
            last_letter = current_word[-1]
            print(f"Your word must start with '{last_letter.upper()}'.")
            player_word = input("Enter your word: ").lower()

            if player_word in used_words:
                print(f"Oops! The word '{player_word}' has already been used. You lose!")
                break

            if player_word[0] != last_letter:
                print(f"Oops! The word must start with '{last_letter.upper()}'. Try again!")
            elif player_word not in words:
                print(f"Oops! '{player_word}' is not a valid word in the category. Try again!")
            else:
                used_words.append(player_word)
                current_word = player_word
                player_turn = False  # Switch to computer's turn
        else:
            # Computer's turn to give a word
            last_letter = current_word[-1]
            valid_words = [word for word in words if word.startswith(last_letter) and word not in used_words]
            if valid_words:
                computer_word = random.choice(valid_words)
                print(f"\nComputer's word: {computer_word.capitalize()}")
                used_words.append(computer_word)
                current_word = computer_word
                player_turn = True  # Switch to player's turn
            else:
                print(f"\nNo more words available for the computer. You win!")
                break

# Start the game
if __name__ == "__main__":
    start_game()
