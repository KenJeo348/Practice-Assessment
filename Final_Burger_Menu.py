"""Final Version of my Burger Menu code
It is assembled with all the updated
versions of my components.
This program allows the user to find,
add, or delete combos from a burger menu.
Created by Kenny Jeong
23/04/2023"""


import easygui


# Function displaying the main menu.
def main_menu():
    # A dictionary containing the pre-existing combo meals.
    menu = {
        "Value Combo":
            {"Beef Burger": 5.69,
             "Fries": 1.00,
             "Fizzy Drink": 1.00},
        "Cheesy Combo":
            {"Cheeseburger": 6.69,
             "Fries": 1.00,
             "Fizzy Drink": 1.00},
        "Super Combo":
            {"Cheeseburger": 6.69,
             "Large Fries": 2.00,
             "Smoothie": 2.00}
    }
    # Continuous loop of main menu until user exits the system
    while True:
        # Find out what the user wants to do in the main menu
        menu_choice = easygui.buttonbox("Welcome to the Main Menu\n"
                                        "Please Choose from below.",
                                        "Main Menu", choices=["Add Combo",
                                                              "Find Combo",
                                                              "Delete Combo",
                                                              "Output Combos",
                                                              "Exit System"])
        # User wants to add a combo
        if menu_choice == "Add Combo":
            # Check if the user wants to add a combo
            yes_no_add = easygui.buttonbox("Do you want to add a new combo?",
                                           "Add Combo Checker",
                                           choices=["Yes", "No"])
            # If the user wants to add a combo, ask for the name of the combo
            if yes_no_add == "Yes":
                # Proceed to the 'add_combo_items' function
                add_combo(menu)

        # If user wants to find a combo, proceed to 'find_combo' function
        elif menu_choice == "Find Combo":
            find_combo(menu)

        # If user wants to delete a combo, proceed to 'delete_combo' function
        elif menu_choice == "Delete Combo":
            delete_combo(menu)

        # If user wants to output combos, proceed to 'output combos' function
        elif menu_choice == "Output Combos":
            output_combos(menu)

        # User choose to exit system
        elif menu_choice == "Exit System":
            # Check if the user really wants to exit the system
            exit_system = easygui.buttonbox("Would you like to exit the "
                                            "program", "Exit System",
                                            choices=["Yes", "No"])
            # If user wants to exit the system, print out a farewell message
            if exit_system == "Yes":
                easygui.msgbox("Thank You for using our program!", "Farewell")
                # Break the main menu loop
                break


# Function used to add items in a combo
def add_combo(menu):
    combo_name = easygui.enterbox("Name of Combo:", "Combo Namer")
    # Add the new combo to the menu
    menu[combo_name] = {}
    # Continuous loop until all items are entered
    while True:
        # Asking for the name of the item for the combo
        combo_item = easygui.enterbox("Name of item for the combo:",
                                      "Item Name")
        # While loop continued until user enters a valid number for the price
        while True:
            # Asking for the price of the item
            item_price = easygui.enterbox("Price for the previous item:",
                                          "Item Price")
            # Attempt to change the entered price into a float
            try:
                item_price = float(item_price)
                # Check if the price is between 0-100 dollars
                # As a price outside that range is insensible for an item price
                if item_price <= 0 or item_price > 100:
                    easygui.msgbox("Please enter a price between 0-100 dollars.",
                                   "Insensible Price")
                else:
                    # Break the loop if answer successfully changes to a float
                    # (And price is between the range of 0-100 dollars)
                    break
            # Display an error message if the answer was not valid.
            except ValueError:
                easygui.msgbox("Please enter a valid price in dollars.",
                               "Value Error")

        # Assign the price as the value of the item(key)
        menu[combo_name][combo_item] = item_price

        # Check if user wants to add another item
        yes_no_item = easygui.buttonbox("Do you want to add another Item?",
                                        "Add Item Checker",
                                        choices=["Yes", "No"])

        # User does not want to add another item.
        if yes_no_item == "No":
            # Proceed to the 'change_combo' function
            # Assign the returned value of the function to 'keep_change_combo'
            keep_change_choice = keep_change_combo(menu, combo_name)
            # Break the loop if the returned value from the 'change_combo'
            # function is 'Keep'
            if keep_change_choice == "Keep":
                break


# A function that displays the details of a combo and allows user to change it
def keep_change_combo(menu, combo_name):
    combo_output = ""

    # Separating each item in the combo for cleaner output
    for items in menu[combo_name]:
        item_output = f"{items}: {menu[combo_name][items]:.2f}\n"
        combo_output += item_output

    # Display details of the combo, and ask if user wants to keep or change
    check_combo_details = easygui.buttonbox(f"Details of Combo\n"
                                            f"Combo Name: {combo_name}\n"
                                            f"Item Details:\n"
                                            f"{combo_output}",
                                            "Check Details",
                                            choices=["Keep", "Change"])

    # User wants to change details of the combo.
    if check_combo_details == "Change":
        # Clear the details for the items in the combo.
        menu[combo_name] = {}
        easygui.msgbox(f"Enter the new details for: {combo_name}")
        # Return that the user wants to change the details of the combo
        return "Change"
    else:
        # Return that the user wants to keep the details of the combo
        return "Keep"


# A function that finds a combo in the menu for the user
def find_combo(menu):
    # Continuous loop that repeats until the user enters an existing combo
    while True:
        # Ask the user for the combo they are looking for
        # Assign the name of the combo to 'wanted_combo'
        wanted_combo = easygui.enterbox("Enter the name of the combo you are "
                                        "looking for:", "Find Combo")

        # Combo that the user entered exists in the menu
        if wanted_combo in menu:
            # Proceed to 'change_combo' function
            keep_change_choice = keep_change_combo(menu, wanted_combo)
            # If the 'change_combo' function returns 'change'
            # Proceed to 'add_combo_items' function to enter the new details
            if keep_change_choice == "Change":
                del menu[wanted_combo]
                add_combo(menu)
            break
        else:
            # Show error message when the entered combo does not exist
            easygui.msgbox("The combo you have entered does not exist.\n"
                           "Please check that you have entered the correct"
                           " details", "Combo Not Found")


# A function that finds a combo in the menu than deletes it
def delete_combo(menu):
    # Check if the user really wants to delete a combo as they may not want to
    delete_combo_check = easygui.buttonbox("Are you sure you want to delete "
                                           "a combo", "Delete Combo Checker",
                                           choices=["Yes", "No"])

    if delete_combo_check == "Yes":
        # Continuous loop that runs until the user enters an existing combo
        while True:
            # Asks user for the name of the combo they wish to delete
            combo_to_delete = easygui.enterbox("Name of combo you want to delete:",
                                               "Combo to Delete")
            # Delete the combo if the combo exists in the menu, then break loop
            if combo_to_delete in menu:
                del menu[combo_to_delete]
                easygui.msgbox(f"'{combo_to_delete}' has been deleted from the "
                               f"menu", "Deleted Combo")
                break
                # Show error message if entered combo does not exist
            else:
                easygui.msgbox("The combo you have entered does not exist.\n"
                               "Please check that you have entered the correct "
                               "details", "Combo Not Found")


# A function that outputs the full menu
def output_combos(menu):
    # Formatting to make output easier to read.
    format_symbol = "-"
    format_sides = format_symbol * 3

    # Prints each combo name.
    for combo_name, combo_details in menu.items():
        print(format_symbol * (len(combo_name) + 6))
        print(f"{format_sides}{combo_name}{format_sides}")
        print(format_symbol * (len(combo_name) + 6))
        total_combo_price = 0

        # Prints the name and price for each item in the combo.
        for key in combo_details:
            print(f"*{key}: ${combo_details[key]}")
            total_combo_price += combo_details[key]
        # Prints the total price of the combo
        print(f"*Total Price:${total_combo_price:.2f}\n")


# Main Routine
main_menu()
