"""
This program calculates the total price of produce purchased at the grocery store.

Author: Justin Rivas
Date Written: 6/18/2021
Version: 1.0.0

"""


apple_quantity = float(input("Please input the amount of apples purchased: "))
pears_quantity = float(input("Please input the amount of pears purchased: "))
peaches_quantity = float(input("Please input the amount of peaches purchased: "))

# Stores the price per pound.
APPLE_PRICE = 0.75
PEAR_PRICE = 0.95
PEACH_PRICE = 0.80
# Sales tax
SALES_TAX = 0.0825

# stores and calculates subtotal of the price of fruit
apple_total = apple_quantity * APPLE_PRICE
pear_total = pears_quantity * PEAR_PRICE
peach_total = peaches_quantity * PEACH_PRICE

#outputs subtotal of each fruit
print(f"\nYour subtotal for the apples you purchased is ${apple_total:.2f}")
print(f"Your subtotal for the pears you purchased is ${pear_total:.2f}")
print(f"Your subtotal for the peaches you purchased is ${peach_total:.2f}")

total = (apple_total + pear_total + peach_total) 
#outputs subtotal of all fruits
print(f"The subtotal for your order is: ${total:.2f}")

sales_tax = total * SALES_TAX

grand_total = total + sales_tax

#outputs the amount of sales tax they owe
print("Sales tax for this order is 8.25%\n")

#outputs grand total of fruits with tax
print(f"The total of all of your fruit with tax is ${grand_total:.2f}")