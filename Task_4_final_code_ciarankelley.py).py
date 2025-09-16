import threading
from datetime import datetime

# Ticket prices and discounts
ticket_prices = {
    "Rider": 29.99,
    "Non-Rider": 9.99,
    "Senior": 16.99,
    "Child": 0
}

discount_rates = {
    "Rider": 0.2,
    "Non-Rider": 0.2,
    "Senior": 0.2,
    "Child": 0
}

ticket_types = []
advanced_booking = False  # Global variable to store input value
user_input = None  # Helper function to handle input with timeout

# Function to handle timed input
def timed_input(prompt, timeout=10):
    global user_input
    user_input = None

    def get_input():
        global user_input
        user_input = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("\nTime expired! Using default value.")
    thread.join()  # Ensure the thread finishes
    return user_input


# Lead Guest Name
def get_guest_name():
    while True:
        guest_name = timed_input("Lead Guest Name: ", timeout=10)
        
        if guest_name and guest_name.isalnum():
            return guest_name.capitalize()
        elif not guest_name:
            print("No input provided. Using default name: Guest.")
            return "Guest"
        else:
            print("Invalid name. Please enter a valid alphanumeric name.")


# Date of Visit
def get_visit_date():
    while True:
        visit_date = timed_input("Date of Visit (DD-MM-YYYY): ", timeout=10)
        date_format = "%d-%m-%Y"
        
        if not visit_date:
            print("No input provided. Using today's date.")
            return datetime.now().strftime(date_format)

        try:
            date_obj = datetime.strptime(visit_date, date_format)
            
            if date_obj.date() > datetime.now().date():
                return visit_date
            else:
                print("Date must be in the future. Try again.")
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")


# Number of Guests
def get_num_guests():
    while True:
        guest_number = timed_input("Number of Guests in Party: ", timeout=10)
        
        if not guest_number:
            print("No input provided. Defaulting to 1 guest.")
            return 1
        
        try:
            num_guests = int(guest_number)
            
            if num_guests > 0:
                return num_guests
            else:
                print("Number of guests must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Guest Tickets
def guest_tickets(num_guests):
    print("\nAvailable tickets: Rider (R), Non-Rider (N), Senior (S), Child under 90cm (C)")
    
    for i in range(num_guests):
        while True:
            ticket_type = timed_input(f"Enter the ticket type for guest {i + 1}: ", timeout=10)
            
            if not ticket_type:
                print("No input provided. Defaulting to 'Child'.")
                ticket_types.append("Child")
                break
            
            ticket_type = ticket_type.strip().upper()
            
            if ticket_type in {"R", "N", "S", "C"}:
                ticket_mapping = {"R": "Rider", "N": "Non-Rider", "S": "Senior", "C": "Child"}
                ticket_types.append(ticket_mapping[ticket_type])
                break
            else:
                print("Invalid ticket type. Please enter R, N, S, or C.")


# Calculate Subtotal
def calculate_subtotal():
    return sum(ticket_prices[ticket] for ticket in ticket_types)


# Calculate Discount
def calculate_discount():
    discounts = []
    
    for ticket in ticket_types:
        discount = ticket_prices[ticket] * discount_rates[ticket]
        discounts.append((ticket, discount))
    
    return discounts


# Print Summary
def print_summary(subtotal, total_discount, total):
    print("\n############## Booking Summary ##############")
    print(f"Lead Guest Name: {lead_guest_name}")
    print(f"Date of Visit: {date_of_visit}")
    print(f"Number of Guests: {num_guests}")
    
    print("\nTicket Details (with Discounts):")
    for ticket, discount in total_discount:
        print(f" - {ticket} Ticket: £{ticket_prices[ticket]:.2f}, Discount: £{discount:.2f}")
    
    print(f"\nSubtotal: £{subtotal:.2f}")
    print(f"Total Discount: £{sum(d[1] for d in total_discount):.2f}")
    print(f"Total to Pay: £{total:.2f}")
    print("#############################################")


# Main Program
while True:
    print("\n###############################################")
    print("###### Fun Land Guest Experience ###########")
    
    # Collecting user inputs
    lead_guest_name = get_guest_name()
    date_of_visit = get_visit_date()
    num_guests = get_num_guests()
    
    guest_tickets(num_guests)
    
    # Calculating subtotal, discount and total
    subtotal = calculate_subtotal()
    total_discount = calculate_discount()
    total = subtotal - sum(d[1] for d in total_discount)
    
    # Printing the booking summary
    print_summary(subtotal, total_discount, total)
    
    # Ask if the user wants to make another booking or exit
    another_booking = timed_input("Do you want to make another booking? (Y/N): ", timeout=10)
    
    if not another_booking or another_booking.strip().upper() != 'Y':
        print("Thank you for using Fun Land Guest Experience!")
        break
