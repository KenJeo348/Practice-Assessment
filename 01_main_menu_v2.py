"""Component 1 (Main Menu)
Based on 01_main_menu_v1.
Made the previous code into a function."""


import easygui


def main_menu():

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
            print("Proceed to Output Combos function\n")

        elif menu_choice == "Exit System":
            print("Proceed to Exit System function\n")


# Main Routine
main_menu()
