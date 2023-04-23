"""Component 6 (Output Combos)
Trial of 06_output_combos_v2
Added empty spaces and formatting
to make output easier to see.
"""


def output_combos():

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
    format_symbol = "-"
    format_sides = format_symbol * 3

    for combo_name, combo_details in menu.items():
        print(format_symbol * (len(combo_name) + 6))
        print(f"{format_sides}{combo_name}{format_sides}")
        print(format_symbol * (len(combo_name) + 6))
        total_combo_price = 0

        for key in combo_details:
            print(f"*{key}: ${combo_details[key]}")
            total_combo_price += combo_details[key]
        print(f"*Total Price:${total_combo_price:.2f}\n")


# Main Routine
output_combos()
