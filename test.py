item1_price = 200.0
item2_price = 400.0
item3_price = 600.0
combo_discount = 0.1  # 10% discount for two unique items
gift_pack_discount = 0.25  # 25% discount for all three items

# Define a function to calculate the total price for selected items


def calculate_total_price(selected_items):

    total_price = 0.0
    # Create a set of unique selected items to apply discounts correctly
    unique_items = set(selected_items)

    if "Item 1" in unique_items:
        total_price += item1_price
    if "Item 2" in unique_items:
        total_price += item2_price
    if "Item 3" in unique_items:
        total_price += item3_price

    # Apply discounts based on the number of unique items
    if len(unique_items) == 2:
        total_price *= (1 - combo_discount)
    elif len(unique_items) == 3:
        total_price *= (1 - gift_pack_discount)

    return total_price


# Calculate combo prices directly
combo1_price = (item1_price + item2_price) * (1 - combo_discount)
combo2_price = (item2_price + item3_price) * (1 - combo_discount)
combo3_price = (item1_price + item3_price) * (1 - combo_discount)
combo4_price = (item1_price + item2_price + item3_price) * \
    (1 - gift_pack_discount)

# Define a function to print the catalog


def print_catalog(selected_items):
    print("Total Price for Selected Items:",
          calculate_total_price(selected_items))
    print("Online Store")
    print("-" * 45)
    print(f"Product(s) {' ' * 30} Price")
    print(f"Item 1 {' '*35}{item1_price}")
    print(f"Item 2 {' '*35}{item2_price}")
    print(f"Item 3 {' '*35}{item3_price}")
    print(f"Combo 1(Item 1 + 2){' '*23}{combo1_price}")
    print(f"Combo 2(Item 2 + 3){' '*23}{combo2_price}")
    print(f"Combo 3(Item 1 + 3){' '*23}{combo3_price}")
    print(f"Combo 4(Item 1 + 2 + 3){' '*19}{combo4_price}")
    print("-" * 45)
    print("For delivery Contact: 76738648")


# List of selected items
selected_items = ["Item 2", "Item 1"]

# Call the print_catalog function to display the catalog
print_catalog(selected_items)
