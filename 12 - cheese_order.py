# takes a user's cheese order and provides a total

min_order = 0.25
max_order = 100.00
price = 7.99

cheese_order = float(input("Enter cheese order weight (numeric value): "))

if cheese_order < min_order:
    print(cheese_order,"is below minimum order amount")
elif cheese_order > max_order:
    print(cheese_order,"is more than currently available stock")
else:
    print("{0:.2f}".format(cheese_order) + " costs $" + "{0:.2f}".format(cheese_order * price))
