"""Component 4 (Find Combo)
Allows the user to look for a combo
in the menu, and displays the details
of the combo they are looking for."""


import easygui


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

    wanted_combo = easygui.enterbox("Enter the name of the combo you are "
                                    "looking for:", "Find Combo")

    if wanted_combo in menu:
        print("Move to 'keep_change_combo' function to display combo "
              "details, \nand then let the user choose to keep or change"
              "the combo details.")
        break

    else:
        easygui.msgbox("The combo you have entered does not exist.\n"
                       "Please check that you have entered the correct"
                       " details", "Combo Not Found")
