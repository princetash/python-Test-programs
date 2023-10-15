item1_price = 200.0
item2_price = 400.0
item3_price = 600.0
combo_discount = 0.1  # 10% discount for two unique items
gift_pack_discount = 0.25  # 25% discount for all three items


# Define a function to calculate the total price for selected items
def calculate_total_price(selected_items):
    total_price = 0.0

    # Calculate individual item prices and count unique items
    item1_price, item2_price, item3_price = 0.0, 0.0, 0.0
    num_unique_items = 0

    if "Item 1" in selected_items:
        item1_price = 200.0
        num_unique_items += 1
    if "Item 2" in selected_items:
        item2_price = 400.0
        num_unique_items += 1
    if "Item 3" in selected_items:
        item3_price = 600.0
        num_unique_items += 1

    # Calculate total price and apply discounts
    total_price = item1_price + item2_price + item3_price
    if num_unique_items == 2:
        total_price *= (1 - combo_discount)
    elif num_unique_items == 3:
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
    print("Selected Items:", selected_items)
    print("Total Price for Selected Items:",
          calculate_total_price(selected_items))
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
    print("For delivery Contact: 76738648")


# Call the print_catalog function to display the catalog
print_catalog("Item 1,  Item 3")

"""This code defines a simple catalog for an online store that calculates the price of commodities that a customer purchases and outputs the selected items and the total price. the code also outputs the cost of other possible combinations of items. The program begins by defining the variables for the prices of each item and the percentages of discounts to be applied in the combo packs and gift pack. The calculate_total_price function takes a list of selected items, then initializes the total cost to 0 and the num_unique_items to 0 after which it updates the prices of each item and increaments num_unique_items if it has been selected. It then calculates the individual item prices and counts unique items after which it sums the individual item prices.
The combo prices are calculated directly using the given discount percentages and stored in variables combo1_price, combo2_price, combo3_price and combo4_price.
the print_catalog function takes the items a customer selects as an arguement and it prints the selected items and the total price by calling the calculate_total_price function. In addition, it prints an online store header and a table displaying the products and their corresponding prices. The table is formatted using the print statent for proper spacing. 
Finally, the last part of the code calls the print_catalog function with two arguements to demonstrate how the catalog works.

The program illustrates several features. The first feature is variable initialization where it assigns variables item1_prince,item2_prince and item3_prince their respective values of price. The second feature is arithmetic operation where the program performes arithmetic operatins to calculate the prices by applying the discounts appropriately to the combo packs. The other feature is function composition, where the function is designed to be reusable meaning it can be called from other parts of the code making it easy to maintain"""
