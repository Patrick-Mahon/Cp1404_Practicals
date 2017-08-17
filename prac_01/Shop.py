number_of_items = int(input("Number of items: "))
if number_of_items <= 0:
    print("Invalid")
    number_of_items = int(input("Number of items: "))

total = 0

while number_of_items > 0:
    cost = int(input("Cost of Items: "))
    total = total + cost
    number_of_items = number_of_items - 1
if total > 100:
    discount = total / 10
    discounted_total = total - discount
    print("$", discounted_total)
else:
    print("$", total)