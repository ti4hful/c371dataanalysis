# A 1 
import json
from collections import defaultdict

# Create an empty list to store parsed JSON objects
restaurant_data = []

file_path = r'C:\Codebase\own projects\C371_DA\4DataProcessingUsingPython\FILEIO\dataset\restaurant.json'
with open(file_path, "r") as file:
    for line in file:
# Parse each line as a JSON object
        data = json.loads(line)
        restaurant_data.append(data)

# Initialize dictionaries to store the statistics
average_score_by_restaurant = {}
minimum_score_by_restaurant = {}
maximum_score_by_restaurant = {}
average_score_by_cuisine_borough = {}
minimum_score_by_cuisine_borough = {}
maximum_score_by_cuisine_borough = {}

# Iterate through the restaurant data
for entry in restaurant_data:
    restaurant_id = entry['restaurant_id']
    cuisine = entry['cuisine']
    borough = entry['borough']
    grades = entry['grades']

# Filter out records with missing or invalid scores
    scores = [grade['score'] for grade in grades if 'score' in grade and grade['score'] is not None]

# If there are no valid scores for this restaurant, skip it
    if not scores:
        continue

# Compute average, minimum, and maximum scores for each restaurant
    average_score_by_restaurant[restaurant_id] = sum(scores) / len(scores)
    minimum_score_by_restaurant[restaurant_id] = min(scores)
    maximum_score_by_restaurant[restaurant_id] = max(scores)

# Compute average, minimum, and maximum scores for each cuisine in each borough
    key = (cuisine, borough)
    if key not in average_score_by_cuisine_borough:
        average_score_by_cuisine_borough[key] = []
    average_score_by_cuisine_borough[key].extend(scores)

# Calculate overall statistics for cuisine/borough combinations
for key in average_score_by_cuisine_borough:
    average_scores = average_score_by_cuisine_borough[key]
    minimum_score_by_cuisine_borough[key] = min(average_scores)
    maximum_score_by_cuisine_borough[key] = max(average_scores)

# Print the results
print("Average Scores by Restaurant:")
for restaurant, score in average_score_by_restaurant.items():
    print(f"Restaurant {restaurant}: {score:.2f}")

print("\nMinimum Scores by Restaurant:")
for restaurant, score in minimum_score_by_restaurant.items():
    print(f"Restaurant {restaurant}: {score}")

print("\nMaximum Scores by Restaurant:")
for restaurant, score in maximum_score_by_restaurant.items():
    print(f"Restaurant {restaurant}: {score}")

print("\nAverage Scores by Cuisine/Borough:")
for (cuisine, borough), scores in average_score_by_cuisine_borough.items():
    average_score = sum(scores) / len(scores)
    print(f"{cuisine} in {borough}: {average_score:.2f}")

print("\nMinimum Scores by Cuisine/Borough:")
for (cuisine, borough), score in minimum_score_by_cuisine_borough.items():
    print(f"{cuisine} in {borough}: {score}")

print("\nMaximum Scores by Cuisine/Borough:")
for (cuisine, borough), score in maximum_score_by_cuisine_borough.items():
    print(f"{cuisine} in {borough}: {score}")