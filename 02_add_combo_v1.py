"""Component 2 (Add Combo)
Allows the user to add a new combo to the menu."""


import easygui


menu = {}
combo_name = easygui.enterbox("Name of Combo:", "Combo Namer")
menu[combo_name] = {}

while True:
    combo_item = easygui.enterbox("Name of item for the combo:",
                                  "Item Name")

    item_price = easygui.integerbox("Price for the previous item:",
                                    "Item Price")

    menu[combo_name][combo_item] = item_price

    yes_no_item = easygui.buttonbox("Do you want to add another Item?",
                                    "Add Item Checker",
                                    choices=["Yes", "No"])

    if yes_no_item == "No":
        break
print(menu)
