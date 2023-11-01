# Cintia Biro-Hajnal 11/1/23
import csv
from functools import reduce

# Function to read car data from a CSV file
def read_car_data_csv(file_path):
    car_data_list = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            car_data_list.append(row)

    return car_data_list

# Function to filter cars by make
def filter_cars_by_make(car_data, make):
    make = make.lower()
    filtered_cars = filter(lambda car: car['make'].lower() == make, car_data)
    return list(filtered_cars)

# Function to filter fuel-efficient cars (City MPG > 35)
def filter_fuel_efficient_cars(car_data):
    filtered_cars = filter(lambda car: int(car['city_mpg']) > 35, car_data)
    return list(filtered_cars)

# Function to filter cars with horsepower greater than 100
def filter_high_horsepower_cars(car_data, min_horsepower=100):
    filtered_cars = filter(lambda car: car['horsepower'].isdigit() and int(car['horsepower']) > min_horsepower, car_data)
    return list(filtered_cars)

# Function to calculate the cost of driving 100 miles in the city for a car
def calculate_cost_100_miles(city_mpg, price_per_gallon, miles_driven=100):
    try:
        city_mpg = int(city_mpg)
        cost = miles_driven / city_mpg * price_per_gallon
        return round(cost, 2)
    except ValueError:
        return None

# Function to calculate the average using reduce
def calculate_average(total, value, count):
    total += value
    count += 1
    return total, count

# Specify the path to your 'car_data.csv' file
csv_file_path = r'own projects\C371_DA\5DataAnalysisandExceptionHandling\ASSIGNMENTS\car_data.csv'

# Call the function to read the CSV file
car_data = read_car_data_csv(csv_file_path)

# Print introductory message
print("Welcome to the Car Data Analysis Program!")

# Get user input for the make of cars
user_input_make = input("Enter the make of the car you are looking for: ")

# Call the filter function to get cars of the specified make
matching_cars = filter_cars_by_make(car_data, user_input_make)

# Print the matching cars
if matching_cars:
    print(f"Cars of Make '{user_input_make}' found in the database:")
    for car in matching_cars:
        print(f"Make: {car['make']}, Model: {car['body_style']}, Price: ${car['price']}")
else:
    print(f"No cars found for the make: {user_input_make}")

# Call the filter function to get fuel-efficient cars
fuel_efficient_cars = filter_fuel_efficient_cars(car_data)

# Print the fuel-efficient cars
if fuel_efficient_cars:
    print("\nFuel-efficient cars (City MPG > 35):")
    for car in fuel_efficient_cars:
        print(f"Make: {car['make']}, Model: {car['body_style']}, City MPG: {car['city_mpg']} MPG")
else:
    print("No fuel-efficient cars found (City MPG > 35).")

# Call the filter function to get cars with horsepower greater than 100
high_horsepower_cars = filter_high_horsepower_cars(car_data, min_horsepower=100)

# Print the high horsepower cars
if high_horsepower_cars:
    print("\nCars with Horsepower > 100:")
    for car in high_horsepower_cars:
        print(f"Make: {car['make']}, Model: {car['body_style']}, Horsepower: {car['horsepower']} HP")
else:
    print("No cars found with Horsepower > 100.")

# Prompt the user to input the current gas cost per gallon
price_per_gallon = float(input("\nEnter the current gas cost per gallon: $"))

# Use the map function to calculate the cost of driving 100 miles in the city for each car
costs_100_miles = list(map(lambda car: calculate_cost_100_miles(car['city_mpg'], price_per_gallon), car_data))

# Calculate the average city MPG using the reduce function
city_mpg_values = [int(car['city_mpg']) for car in car_data]
average_city_mpg, _ = reduce(lambda acc, value: calculate_average(acc[0], value, acc[1]), city_mpg_values, (0, 0))
average_city_mpg = average_city_mpg / len(city_mpg_values)

# Calculate the average highway MPG using the reduce function
highway_mpg_values = [int(car['highway_mpg']) for car in car_data]
average_highway_mpg, _ = reduce(lambda acc, value: calculate_average(acc[0], value, acc[1]), highway_mpg_values, (0, 0))
average_highway_mpg = average_highway_mpg / len(highway_mpg_values)

# Calculate the average cost using the reduce function
valid_costs = [cost for cost in costs_100_miles if cost is not None]
average_cost, _ = reduce(lambda acc, value: calculate_average(acc[0], value, acc[1]), valid_costs, (0, 0))
average_cost = average_cost / len(valid_costs)

# Print the results
print("\nSummary:")
print(f"Total number of cars in the database: {len(car_data)}")
print(f"Average City MPG across all cars: {average_city_mpg:.2f} MPG")
print(f"Average Highway MPG across all cars: {average_highway_mpg:.2f} MPG")
print(f"Average Cost of driving 100 miles in the city across all cars: ${average_cost:.2f}")
