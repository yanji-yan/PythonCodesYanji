item = input("What item do you want to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many do you want to buy? "))
total = price * quantity

print(f"You bought {quantity} {item}(s)")
print(f"The total cost is: ${total:}")
