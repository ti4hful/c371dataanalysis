# 1 
# Accept integers from the user and find values lower than the average
def accept_integers():
    numbers = []
    while len(numbers) < 10:
        num = input("Enter an integer (or 'stop' to finish): ")
        if num.lower() == 'stop':
            break
        try:
            num = int(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    if len(numbers) < 5:
        print("You entered less than five numbers.")
        return

    threshold = sum(numbers) / len(numbers)
    
    def find_lower(numbers, threshold):
        return [num for num in numbers if num < threshold]
    
    lower_values = find_lower(numbers, threshold)
    print("Values lower than the average:", lower_values)

accept_integers()

# 2 
# Replace occurrences of a group of characters in a string
def replace_string(input_str, target, replacement):
    return input_str.replace(target, replacement)

input_str = "this is a test. this is just an example."
target = "this is"
replacement = "this will be"

result = replace_string(input_str, target, replacement)
print(result)


# 3 
# Create a simple calculator function
def simple_calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

result = simple_calculator(num1, num2, operation)
print("Result:", result)

# 4  
class BuildingGPS:
    def __init__(self, address, gps_coordinates):
        self.address = address
        self.gps_coordinates = gps_coordinates

class Building3D:
    def __init__(self, size, position):
        self.size = size
        self.position = position
class AirplaneATC:
    def __init__(self, flight_number, altitude, speed):
        self.flight_number = flight_number
        self.altitude = altitude
        self.speed = speed

class AirplaneSimulator:
    def __init__(self, model, pilot_name):
        self.model = model
        self.pilot_name = pilot_name
class CarInventory:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

class CarGame:
    def __init__(self, player_name, speed):
        self.player_name = player_name
        self.speed = speed
class IceCreamDairy:
    def __init__(self, flavor, ingredients, production_date):
        self.flavor = flavor
        self.ingredients = ingredients
        self.production_date = production_date

class IceCreamStock:
    def __init__(self, stock_id, quantity, expiration_date):
        self.stock_id = stock_id
        self.quantity = quantity
        self.expiration_date = expiration_date
class BookPublishing:
    def __init__(self, title, author, genre, word_count):
        self.title = title
        self.author = author
        self.genre = genre
        self.word_count = word_count

class BookCatalog:
    def __init__(self, isbn, title, author, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre

# 5 
class House(BuildingGPS):
    def __init__(self, address, gps_coordinates, bedrooms, bathrooms):
        super().__init__(address, gps_coordinates)
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

class OfficeBuilding(Building3D):
    def __init__(self, size, position, office_count):
        super().__init__(size, position)
        self.office_count = office_count
