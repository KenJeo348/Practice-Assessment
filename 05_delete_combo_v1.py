"""Component 5 (Delete Combo)
Allows user to search for a combo
and then delete that combo."""


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
    combo_to_delete = easygui.enterbox("Name of combo you want to delete:",
                                       "Combo to Delete")
    if combo_to_delete in menu:
        del menu[combo_to_delete]
        easygui.msgbox(f"'{combo_to_delete}' has been deleted from the "
                       f"menu", "Deleted Combo")
        break
    else:
        easygui.msgbox("The combo you have entered does not exist.\n"
                       "Please check that you have entered the correct "
                       "details", "Combo Not Found")
print(menu)
