"""Component 3 (Keep or Change Combo)
Shows the details of a specific combo,
and asks the user if they want to keep
or change the details of that combo."""


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
    print("User decides to change the details of the current combo.")
elif check_combo_details == "Keep":
    print("User wants to keep the details of the current combo.")
