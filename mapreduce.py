import json
from collections import defaultdict
# Step 1 
try:
    with open(r'own projects/C371_DA/5DataAnalysisandExceptionHandling/ASSIGNMENTS/test.json', 'r') as file:
        dataset = json.load(file)
except FileNotFoundError:
    print("Error: The input file is missing or the path is incorrect.")
except json.JSONDecodeError:
    print("Error: The input file is not a valid JSON file.")

# Step 2
from datetime import datetime

try:
    def convert_timestamps(restaurant):
        if "grades" in restaurant:
            for grade in restaurant["grades"]:
                try:
                    grade["date"] = datetime.utcfromtimestamp(grade["date"] / 1000).strftime('%Y-%m-%d')
                except Exception:
                    print("Error: Failed to convert a timestamp.")
        return restaurant

    dataset = list(map(lambda restaurant: convert_timestamps(restaurant), dataset))
except Exception:
    print("Error: An unexpected error occurred during timestamp conversion.")

# Step 3
def has_at_least_5_reviews(restaurant):
    return "grades" in restaurant and len(restaurant["grades"]) >= 5

restaurants_with_5_or_more_reviews = list(filter(has_at_least_5_reviews, dataset))

# Step 4

from datetime import datetime

from collections import defaultdict

most_recent_year = 0

for restaurant in dataset:
    if "grades" in restaurant:
        for grade in restaurant["grades"]:
            if "date" in grade:
                date_str = grade["date"]["$date"]
                date = datetime.fromtimestamp(int(date_str) / 1000)
                year = date.year
                most_recent_year = max(most_recent_year, year)

reviews_per_year = defaultdict(int)

for restaurant in dataset:
    if "grades" in restaurant:
        for grade in restaurant["grades"]:
            if "date" in grade:
                date_str = grade["date"]["$date"]
                date = datetime.fromtimestamp(int(date_str) / 1000)
                year = date.year
                reviews_per_year[restaurant["name"]] += 1 if year == most_recent_year else 0

restaurants_with_5_or_more_reviews_in_recent_year = list(filter(lambda restaurant: reviews_per_year[restaurant["name"]] >= 5, dataset))

from functools import reduce

total_reviews = reduce(lambda acc, restaurant: acc + len(restaurant["grades"]) if "grades" in restaurant else acc, dataset, 0)

average_reviews_per_restaurant = total_reviews / len(dataset)

restaurants_with_more_reviews_than_average = list(filter(lambda restaurant: len(restaurant["grades"]) > average_reviews_per_restaurant if "grades" in restaurant else False, dataset))

# Summary of results
print("Number of restaurants in the dataset:", len(dataset))
print("Number of restaurants with at least 5 reviews:", len(restaurants_with_5_or_more_reviews))
print("Number of restaurants with at least 5 reviews in the most recent year:", len(restaurants_with_5_or_more_reviews_in_recent_year))
print("Average number of reviews per restaurant:", average_reviews_per_restaurant)
print("Number of restaurants with more reviews than the average:", len(restaurants_with_more_reviews_than_average))