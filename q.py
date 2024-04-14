
item_no=input("Enter the item number: ")
item_price=input("Enter the item price: ")
discount=input("Enter the dicount (0.10 for 10%): ")
quantity=input("Quantity: ")

total=float(item_price)*float(quantity)
net_total=total-total*float(discount)

print("Your Total is: "+str(net_total))