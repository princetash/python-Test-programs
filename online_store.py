def online_store_catalog(item1_price, item2_price, item3_price, combo_discount, gift_pack_discount):
    # Calculate combo prices directly
    combo1_price = (item1_price + item2_price) * (1 - combo_discount)
    combo2_price = (item2_price + item3_price) * (1 - combo_discount)
    combo3_price = (item1_price + item3_price) * (1 - combo_discount)
    combo4_price = (item1_price + item2_price + item3_price) * \
        (1 - gift_pack_discount)
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
    print('-' * 45)
    print("For delivery Contact:98764678899")


# Define item prices and discounts
item1_price = 200.0
item2_price = 400.0
item3_price = 600.0
combo_discount = 0.10  # 10% discount for two unique items
gift_pack_discount = 0.25  # 25% discount for all three items

# Call the online_store function with the defined prices and discounts
online_store_catalog(item1_price, item2_price, item3_price,
                     combo_discount, gift_pack_discount)

"""This code defines a simple catalog for an online store that calculates the price of commodities that a customer purchases and outputs the items and the total price. The code also outputs the cost of other possible combinations of items. The program defines the variables for the prices of each item and the percentages of discounts to be applied in the combo packs and gift pack. 
The combo prices are calculated directly using the given discount percentages and stored in variables combo1_price, combo2_price, combo3_price and combo4_price respectively.
The online_store_catalog function takes the items prices as arguements and it prints the selected items and the total price by calculating the total prices while applying the discounts where necessary. In addition, it prints an online store header and a table displaying the products and their corresponding prices. The table is formatted using the print statement for proper spacing. 
Finally, the last part of the code calls the print_catalog function with the arguements to demonstrate how the catalog works.

The program illustrates several features. The first feature is variable initialization where it assigns variables item1_prince,item2_prince and item3_prince their respective values of price. The second feature is arithmetic operation where the program performes arithmetic operations to calculate the prices by applying the discounts appropriately to the combo packs. The other feature is function composition, where the function is designed to be reusable meaning it can be called from other parts of the code making it easy to maintain. In addition, since the item prices are passed dynamically, it is easy to edit the prices and the discount percentages easily without affecting the program"""
