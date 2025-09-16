import pandas as pd
import matplotlib.pyplot as plt  # Importing for pie chart display

# Function to calculate total revenue for the selected date range
def total_sales_revenue(startdate, enddate):
    data_frame = pd.read_csv("Task4a_data.csv")
    
    # Filter data by date range
    df_filtered = data_frame[(data_frame['Date'] >= startdate) & (data_frame['Date'] <= enddate)]
    
    # Calculate revenue as quantity sold * price
    df_filtered['Revenue'] = df_filtered['Quantity'] * df_filtered['Price']
    
    # Sum up the revenue for the specified period
    total_revenue = df_filtered['Revenue'].sum()
    return total_revenue

# Function to calculate total sales for each item within a date range
def total_items_sold(startdate, enddate):
    data_frame = pd.read_csv("Task4a_data.csv")
    
    # Filter data by date range
    df_filtered = data_frame[(data_frame['Date'] >= startdate) & (data_frame['Date'] <= enddate)]
    
    # Calculate total sales by summing 'Quantity' grouped by 'Item'
    total_sales = df_filtered.groupby('Item')['Quantity'].sum()
    return total_sales

# Menu function to get main menu choice
def menu():
    while True:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item")
        print("2. Show total sales of all items")
        print("3. Show total sales revenue")
        print("4. Exit")
        
        main_menu_choice = input("Please enter the number of your choice (1-4): ")
        try:
            main_menu_choice = int(main_menu_choice)
            if main_menu_choice < 1 or main_menu_choice > 4:
                print("Sorry, you did not enter a valid choice")
                continue
            else:
                return main_menu_choice
        except ValueError:
            print("Sorry, you did not enter a valid choice")

# Function to get product choice
def get_product_choice():
    while True:
        print("######################################################")
        print("Please choose a product from the list:")
        print("1.  T-Shirt")
        print("2.  Keyring")
        print("3.  Mug")
        print("4.  Cap")
        print("5.  Toy")
        print("6.  Poster")
        print("7.  Magnet")
        print("8.  Pen")
        print("######################################################")
        
        shop_list = ["T-Shirt", "Keyring", "Mug", "Cap", "Toy", "Poster", "Magnet", "Pen"]
        item_choice = input("Please enter the number of your choice (1-8): ")
        try:
            item_choice = int(item_choice)
            if item_choice < 1 or item_choice > 8:
                print("Sorry, you did not enter a valid choice")
            else:
                item_name = shop_list[item_choice - 1]
                return item_name
        except ValueError:
            print("Sorry, you did not enter a valid choice")

# Function to get start date
def get_start_date():
    while True:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date, dayfirst=True)
            return start_date
        except ValueError:
            print("Sorry, you did not enter a valid date")

# Function to get end date
def get_end_date():
    while True:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date, dayfirst=True)
            return end_date
        except ValueError:
            print("Sorry, you did not enter a valid date")

# Function to get selected item sales data
def get_selected_item(item, startdate, enddate):
    df = pd.read_csv("Task4a_data.csv")
    df_filtered = df[(df['Item'] == item) & (df['Date'] >= startdate) & (df['Date'] <= enddate)]
    return df_filtered

# Main loop
while True:
    main_menu = menu()
    
    if main_menu == 1:
        # Option 1: Show total sales for a specific item
        item = get_product_choice()
        start_date = get_start_date()
        end_date = get_end_date()
        sales_data = get_selected_item(item, start_date, end_date)
        print(sales_data)
    
    elif main_menu == 2:
        # Option 2: Show total sales of all items
        start_date = get_start_date()
        end_date = get_end_date()
        total_sales = total_items_sold(start_date, end_date)
        print("Total sales of all items:")
        print(total_sales)
    
    elif main_menu == 3:
        # Option 3: Show total sales revenue
        start_date = get_start_date()
        end_date = get_end_date()
        revenue = total_sales_revenue(start_date, end_date)
        print(f"Total revenue from {start_date} to {end_date} is: {revenue}")
    
    elif main_menu == 4:
        # Option 4: Quit the program
        print("Exiting the program.")
        break  # Quit the program
