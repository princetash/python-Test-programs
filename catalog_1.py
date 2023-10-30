item_prices = {
    'Item 1': 200.0,
    'Item 2': 400.0,
    'Item 3': 600.0,
}


def calculate_total_price(selected_items):
    # Calculate the total price based on selected items
    total_price = 0.0

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


def calculate_combo_prices(selected_items):
    combo_prices = {}

    # Calculate combo prices based on selected items
    if 'Item 1' in selected_items and 'Item 2' in selected_items:
        combo_prices['Combo 1(Item 1 + 2)'] = item_prices['Item 1'] + \
            item_prices['Item 2']
    if 'Item 2' in selected_items and 'Item 3' in selected_items:
        combo_prices['Combo 2(Item 2 + 3)'] = item_prices['Item 2'] + \
            item_prices['Item 3']
    if 'Item 1' in selected_items and 'Item 2' in selected_items and 'Item 3' in selected_items:
        combo_prices['Combo 3(Item 1 + 2 + 3)'] = item_prices['Item 1'] + \
            item_prices['Item 2'] + item_prices['Item 3']

    return combo_prices


def print_catalog():
    print("Online Store")
    print("-" * 45)
    print("Product(s)\t\t\t\tPrice")
    items = item_prices

    # Print individual item prices
    for item, price in items.items():
        print(f"{item}\t\t\t\t{price}")

    # Allow the user to choose items
    selected_items = []
    print("Available Items:")
    for item in item_prices:
        print(item)
    while True:
        item_choice = input("Enter the item you want (or 'done' to finish): ")
        if item_choice == 'done':
            break
        elif item_choice in item_prices:
            selected_items.append(item_choice)
        else:
            print("Invalid item choice. Please choose from the available items.")

    # Calculate and print the total price
    total_price = calculate_total_price(selected_items)
    print(f"Total Price for Selected Items: {total_price}")

    # Calculate and print combo prices
    combo_prices = calculate_combo_prices(selected_items)
    for combo, price in combo_prices.items():
        print(f"{combo}\t\t\t\t{price}")

    print("-" * 45)
    print("For delivery Contact: 76738648")


# Example usage:
print_catalog()
