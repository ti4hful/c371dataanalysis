# Cintia Biro-Hajnal 2023-10-19

# 1. Ask the user what size cup they want, choosing between small, medium, and large
size = input("Do you want small, medium, or large? ").lower()

# 2. Ask the user what kind of coffee they want, choosing between brewed, espresso, and cold brew
coffee_type = input("What kind of coffee do you want? Please select the type of coffee you would like from the following options brewed / espresso / cold brew : ").lower()

# 3. Ask the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel
flavor_choice = input("Would you like to add flavored syrup? Please answer this with a yes or no : ").lower()

if flavor_choice == "yes":
    # If the user wants to add flavoring, so the answer is yes: 
    flavor = input("Then, please choose a flavor from the following options: Hazelnut / Vanilla / Caramel / None : ").lower()
else:
    # If the user doesn't want flavoring, set the flavor to "none"
    flavor = "none"

# 5. Display a statement that summarizes what the user ordered
print(f"You ordered a {size} size of {coffee_type} coffee with {flavor} flavored syrup.")

# 4. Calculate the price of the cup using the following values:
    # Size:
        # small: $2
        # medium: $3
        # large: $4

    # Type:
        # brewed: no additional cost
        # espresso: 50 cents
        # cold brew: $1

    # Flavoring:
        # None: no additional cost
        # All other options: 50 cents

# Prices for different options
size_prices = {"small": 2, "medium": 3, "large": 4}
type_prices = {"brewed": 0, "espresso": 0.5, "cold brew": 1}
flavor_prices = {"none": 0, "hazelnut": 0.5, "vanilla": 0.5, "caramel": 0.5}

# Calculate the cost of the coffee based on user's choices
total_cost = size_prices.get(size, 0) + type_prices.get(coffee_type, 0) + flavor_prices.get(flavor, 0)


# 6. Display the total cost of the cup of coffee as well as the cost with a 15% tip, in phrases that explain the values to the user
    # Round the cost with tip to two decimal places
tip_percentage = 15
tip = total_cost * (tip_percentage / 100)
total_cost_with_tip = total_cost + tip

# Display the total cost and cost with a tip to the user
print(f"The total cost of your coffee is ${total_cost:.2f}.")
print(f"If you are satisfied with the service and would like to leave with a {tip_percentage}% tip, the total cost is ${total_cost_with_tip:.2f}.")

