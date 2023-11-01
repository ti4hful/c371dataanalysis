# Cintia Biro-Hajnal 25/10/23

# Implement the classes listed below
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Burger(FoodItem):
    def __init__(self, name, price, condiments):
        super().__init__(name, price)
        self.condiments = condiments

class Drink(FoodItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

class Side(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Combo(FoodItem):
    def __init__(self, burger, side, drink):
        name = f"{burger.name} Combo"
        price = burger.price + side.price + drink.price
        super().__init__(name, price)
        self.burger = burger
        self.side = side
        self.drink = drink

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

# Sample menu items
menu = {
    "burger": Burger("Classic Burger", 5.99, ["Lettuce", "Tomato", "Cheese"]),
    "drink": Drink("Soda", 1.99, "Medium"),
    "side": Side("Fries", 2.49),
}

def display_menu():
    print("Menu:")
    for item_type, item in menu.items():
        print(f"{item_type.capitalize()}: {item.name} - ${item.price:.2f}")

def user_input_burger():
    print("Select a burger:")
    display_menu()
    while True:
        choice = input("Enter your choice (e.g., 'burger'): ").lower()
        if choice == "burger":
            return menu[choice]
        else:
            print("Invalid choice. Please select a burger.")

def user_input_drink():
    print("Select a drink:")
    display_menu()
    while True:
        choice = input("Enter your choice (e.g., 'drink'): ").lower()
        if choice == "drink":
            return menu[choice]
        else:
            print("Invalid choice. Please select a drink.")

def user_input_side():
    print("Select a side:")
    display_menu()
    while True:
        choice = input("Enter your choice (e.g., 'side'): ").lower()
        if choice == "side":
            return menu[choice]
        else:
            print("Invalid choice. Please select a side.")

def user_input_combo():
    print("Build your combo:")
    burger = user_input_burger()
    side = user_input_side()
    drink = user_input_drink()
    return Combo(burger, side, drink)

def take_order():
    print("Welcome to Burger Shop")
    customer_name = input("Please enter your name: ")
    order = Order()

    while True:
        print("What would you like to order?")
        print("1. Burger")
        print("2. Drink")
        print("3. Side")
        print("4. Combo (Burger, Side, and Drink)")
        print("5. Finish and view order")
        print("6. Cancel order")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            order.add_item(user_input_burger())
        elif choice == "2":
            order.add_item(user_input_drink())
        elif choice == "3":
            order.add_item(user_input_side())
        elif choice == "4":
            order.add_item(user_input_combo())
        elif choice == "5":
            print(f"Order for {customer_name}:")
            for item in order.items:
                print(f"{item.name}: ${item.price:.2f}")
            total_price = order.calculate_total()
            print(f"Total: ${total_price:.2f}")
            print("Thank you for your business!")
            break
        elif choice == "6":
            print("Order canceled. Thank you for considering us.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

take_order()
