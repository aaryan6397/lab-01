#  Profit or Loss

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))
if selling_price > cost_price:
    print("Profit of:", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss of:", cost_price - selling_price)
else:
    print("No Profit No Loss")