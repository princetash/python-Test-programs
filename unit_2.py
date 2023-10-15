item_prices = {
    'Item 1': 200.0,
    'Item 2': 400.0,
    'Item 3': 600.0,
}


def calculate_total_price(selected_items):
    # Initialize total_price
    total_price = 0.0

    # Calculate the total price based on selected items
    for item in selected_items:
        if item in item_prices:
            total_price += item_prices[item]

    # Apply discounts for combo packs
    if 'Item 1' in selected_items and 'Item 2' in selected_items:
        total_price *= 0.9
    if 'Item 2' in selected_items and 'Item 3' in selected_items:
        total_price *= 0.9
    if 'Item 1' in selected_items and 'Item 2' in selected_items and 'Item 3' in selected_items:
        total_price *= 0.75

    return total_price


def print_catalog():
    print("Online Store")
    print("-" * 45)
    print("Product(s)\t\t\t\tPrice")

    for item, price in item_prices.items():
        print(f"{item}\t\t\t\t{price}")


def calculate_combo_price(items):
    combo_price = 0.0

    # Check if Item 1 and Item 2 are in the selected items
    if 'Item 1' in items and 'Item 2' in items:
        combo_price += item_prices['Item 1'] + item_prices['Item 2']

    # Check if Item 2 and Item 3 are in the selected items
    if 'Item 2' in items and 'Item 3' in items:
        combo_price += item_prices['Item 2'] + item_prices['Item 3']

    # Check if Item 1, Item 2, and Item 3 are in the selected items
    if 'Item 1' in items and 'Item 2' in items and 'Item 3' in items:
        combo_price += item_prices['Item 1'] + \
            item_prices['Item 2'] + item_prices['Item 3']

    return combo_price


# Inside the main code, calculate combo prices
combo1_price = calculate_combo_price(['Item 1', 'Item 2'])
combo2_price = calculate_combo_price(['Item 2', 'Item 3'])
combo3_price = calculate_combo_price(['Item 1', 'Item 2', 'Item 3'])

# Print combo pack prices
print(f"Combo 1(Item 1 + 2)\t\t{combo1_price}")
print(f"Combo 2(Item 2 + 3)\t\t{combo2_price}")
print(f"Combo 3(Item 1 + 2 + 3)\t\t{combo3_price}")


print("-" * 45)
print("For delivery Contact: 76738648")


# Allow the user to choose items
selected_items = []
print("Available Items:")
for item in item_prices:
    print(item)
while True:
    item_choice = input(
        "Enter the item you want (or 'done' to finish): ")
    if item_choice == 'done':
        break
    elif item_choice in item_prices:
        selected_items.append(item_choice)
    else:
        print("Invalid item choice. Please choose from the available items.")

# Calculate and print the total price
total_price = calculate_total_price(selected_items)
print(f"Total Price for your Selected Items: {total_price}")

# Print the catalog
print_catalog()
