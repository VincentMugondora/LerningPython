# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {food}: $"))
        foods.append(food)
        prices.append(price)
print()
print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nTotal: ${total}")