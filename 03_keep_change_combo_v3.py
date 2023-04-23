"""Component 3 (Keep or Change Combo)
Based on 03_keep_change_combo
Previous code made into a function"""


import easygui


def keep_change_combo():
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
    combo_name = "Value Combo"
    combo_output = ""

    for items in menu[combo_name]:
        item_output = f"{items}: {menu[combo_name][items]:.2f}\n"
        combo_output += item_output

    check_combo_details = easygui.buttonbox(f"Details of Combo\n"
                                            f"Combo Name: {combo_name}\n"
                                            f"Item Details:\n"
                                            f"{combo_output}",
                                            "Check Details",
                                            choices=["Keep", "Change"])

    if check_combo_details == "Change":
        menu[combo_name] = {}
        easygui.msgbox(f"Enter the new details for: {combo_name}")
        print("Proceed to 'Add Combo' function so that user can add the new"
              " details for the combo.")
        # So that other functions know that user wants to change the details
        return "Change"

    elif check_combo_details == "Keep":
        print("Program continues without changing details of the combo.")
        # So that other functions know that user wants to keep the details
        return "Keep"


# Main Routine
keep_change_combo()
