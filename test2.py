# Set up individual item prices and discounts
item1_price = 200.0
item2_price = 400.0
item3_price = 600.0
combo_discount = 0.1  # 10% discount for two unique items
gift_pack_discount = 0.25  # 25% discount for all three items

# Calculate combo prices directly
combo1_price = (item1_price + item2_price) * (1 - combo_discount)
combo2_price = (item2_price + item3_price) * (1 - combo_discount)
combo3_price = (item1_price + item3_price) * (1 - combo_discount)
combo4_price = (item1_price + item2_price + item3_price) * \
    (1 - gift_pack_discount)

# Define a function to print the catalog


def print_catalog(selected_items):
    print("Selected Items:", selected_items)
    print("Online Store")
    print("-" * 45)
    print("Product(s) ", ' ' * 30, " Price")
    print("Item 1 ", ' '*35, item1_price)
    print("Item 2 ", ' '*35, item2_price)
    print("Item 3 ", ' '*35, item3_price)
    print("Combo 1(Item 1 + 2)", ' '*23, combo1_price)
    print("Combo 2(Item 2 + 3)", ' '*23, combo2_price)
    print("Combo 3(Item 1 + 3)", ' '*23, combo3_price)
    print("Combo 4(Item 1 + 2 + 3)", ' '*19, combo4_price)
    print("-" * 45)
    print("For delivery Contact: 98764678899")


# List of selected items (you can modify this as needed)
selected_items = ["Item 1"]

# Call the print_catalog function to display the catalog
print_catalog(selected_items)
