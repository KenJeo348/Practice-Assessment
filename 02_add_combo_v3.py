"""Component 2 (Add Combo)
Based on 02_add_combo_v2
Previous code changed into a function."""


import easygui


def add_combo():
    menu = {}
    combo_name = easygui.enterbox("Name of Combo:", "Combo Namer")
    menu[combo_name] = {}

    while True:
        combo_item = easygui.enterbox("Name of item for the combo:",
                                      "Item Name")
        while True:
            item_price = easygui.enterbox("Price for the previous item:",
                                          "Item Price")
            try:
                item_price = float(item_price)
                break
            except ValueError:
                easygui.msgbox("Please enter a valid price in dollars.",
                               "Value Error")

        menu[combo_name][combo_item] = item_price

        yes_no_item = easygui.buttonbox("Do you want to add another Item?",
                                        "Add Item Checker",
                                        choices=["Yes", "No"])

        if yes_no_item == "No":
            print("Proceed to 'keep_change_combo' function so that the user can "
                  "check and maybe change their combo details.")
            break


# Main Routine
add_combo()
