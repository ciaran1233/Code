import pandas as pd
import matplotlib.pyplot as plt  # Importing for pie chart display

# Function to calculate total sales for each item
def total_items_sold(startdate, enddate):
    data_frame = pd.read_csv("Task4a_data.csv")
    total = data_frame.groupby(['Item']).sum()
    total_out = total.loc[:, startdate:enddate].sum(axis=1, numeric_only=True)
    return total_out

def menu():
    

    flag = True
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item")
        print("2. Show total sales of all items")
        print("3. show total sales revenue")
        main_menu_choice = input("Please enter the number of your choice (1-3): ")
        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
                if int(main_menu_choice) < 1 or int(main_menu_choice) > 2: or int(main_menu_choice)>:
                print("Sorry, you did not enter a valid choice")
                flag = True
        else:
            return int(main_menu_choice)

# Function to get product choice
def get_product_choice():
    flag = True
    while flag:
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
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = shop_list[int(item_choice)-1]
                return item_name

# Function to get start date
def get_start_date():
    flag = True
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    return start_date

# Function to get end date
def get_end_date():
    flag = True
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')
        try:
            pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    return end_date

# Function to get selected item sales data
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv")
    df2 = df1.loc[df1['Item'] == item]
    df3 = df2.loc[:, startdate:enddate]
    return df3

# Main loop
while True:
    main_menu = menu()
    
    if main_menu == 1:
        item = get_product_choice()
        start_date = get_start_date()
        end_date = get_end_date()

        extracted_data = get_selected_item(item, start_date, end_date)

        print("\n")
        print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
        extract_no_index = extracted_data.to_string(index=False)
        print(extract_no_index)
        print("\n")

    elif main_menu == 2:
        startdate = get_start_date()
        enddate = get_end_date()

        extracted = total_items_sold(startdate, enddate)
        print("\nThe total sales between {} and {} were:".format(startdate, enddate))
        print(extracted)

        # Step 1: Find the max value (highest units sold)
        max_values = extracted.max()
        
        # Step 2: Get the name of the best selling item
        max_label = extracted.idxmax()

        # Step 3: Print the result
        print("\nThe most popular product between {} and {} was {}s with {} units sold.".format(startdate, enddate, max_label, max_values))

        # Step 4: Ask if the user wants to view a pie chart
        my_input = input("\nWould you like to see a pie chart of the sales data? (Y/N): ").upper()

        if my_input == "Y":
            # Step 5: Display a pie chart
            plt.figure(figsize=(7, 7))
            extracted.plot(kind="pie", autopct='%1.1f%%', labels=extracted.index, startangle=90)
            plt.title("Sales Distribution between {} and {}".format(startdate, enddate))
            plt.ylabel("")  # Hide the ylabel for cleaner display
            plt.show()

    else:
        print("Thank you for using the dashboard")
        exit()
