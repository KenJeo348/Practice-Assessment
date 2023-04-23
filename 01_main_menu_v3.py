"""Component 1 (Main Menu)
Based on 01_main_menu_v2
Added a menu containing the
pre-existing combos."""


import easygui


def main_menu():

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

    while True:
        menu_choice = easygui.buttonbox("Welcome to the Main Menu\n"
                                        "Please Choose from below.",
                                        "Main Menu", choices=["Add Combo",
                                                              "Find Combo",
                                                              "Delete Combo",
                                                              "Output Combos",
                                                              "Exit System"])

        if menu_choice == "Add Combo":
            print("Proceed to Add Combo function.\n")

        elif menu_choice == "Find Combo":
            print("Proceed to Find Combo function.\n")

        elif menu_choice == "Delete Combo":
            print("Proceed to Delete Combo function.\n")

        elif menu_choice == "Output Combos":
            # Brief check to see if menu contains all the information
            print(menu)

        elif menu_choice == "Exit System":
            print("Proceed to Exit System function\n")


# Main Routine
main_menu()
