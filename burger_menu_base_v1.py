"""Base for Burger Menu Combos code
Assembling the components
to make up the final code."""


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
            print("Proceed to 'Find Combo' function/component")

        # If user wants to delete a combo, proceed to 'delete_combo' function
        elif menu_choice == "Delete Combo":
            print("Proceed to 'Delete Combo' function/component")

        # If user wants to output combos, proceed to 'output combos' function
        elif menu_choice == "Output Combos":
            print("Proceed to 'Output Combos' function/component")

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


# Main Routine
main_menu()
