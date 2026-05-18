menu = {
    "pizza": 10.0,
    "burger": 8.0,
    "fries": 3.0,
    "soda": 2.0,
    "chicken": 12.0
}
cart = []
total = 0

for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("------ Menu -------")
while True:
    food = input("Select food item (q to quit): ").lower()
    if food == "q":
        break;
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not on menu. Please select again.")
print("--------------------")
print("---- Your order -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print(f"\nTotal: ${total:.2f}")