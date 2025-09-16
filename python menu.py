def menu_selection(option):
    menu_options = {
        '1': 'start new game', 
        '2': 'load game',
        '3': 'Adult', 
        '4': 'Senior', 
        'q': 'Quit'
    }
    return menu_options.get(option, "Invalid option. Please try again.")

def display_menu():
    print("Please select an option from the menu:") 
    print("1 - start new game") 
    print("2 - load game") 
    print("3 - Adult") 
    print("4 - Senior") 
    print("q - Quit") 

while True:
    display_menu() 
    user_input = input("Enter your choice: ") 
    selected_option = menu_selection(user_input)
    
    if user_input == 'q': 
        print("Exiting the program.")
        break
    else: 
        print(f"You selected: {selected_option}")