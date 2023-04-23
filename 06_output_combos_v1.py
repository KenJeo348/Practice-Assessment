"""Component 6 (Output Combos)
Outputs all the existing combos
in the menu."""

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

for combo_name, combo_details in menu.items():
    print(f"Combo Name: {combo_name}")
    total_combo_price = 0

    for key in combo_details:
        print(f"{key}: {combo_details[key]}")
        total_combo_price += combo_details[key]
    print(f"Total Price:{total_combo_price:.2f}")
