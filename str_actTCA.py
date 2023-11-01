import string

# Function to remove punctuation and count word frequency
def analyze_text(text):
    # Convert to lowercase
    text = text.lower()
    # Split the text into words
    words = text.split()
    # Remove punctuation from words
    words_clean = [word.strip(string.punctuation) for word in words if word.strip(string.punctuation)]
    # Count word frequency using a dictionary
    word_freq = {}
    for word in words_clean:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

# Function to sort the dictionary alphabetically
def sort_alphabetically(word_freq):
    sorted_dict = dict(sorted(word_freq.items()))
    return sorted_dict

# Function to sort the dictionary by frequency
def sort_by_frequency(word_freq, reverse=True):
    sorted_dict = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=reverse))
    return sorted_dict

# User input for text
user_text = input("Enter text: ")

# Analyze the user's text
result = analyze_text(user_text)

# Sort the dictionary alphabetically
sorted_alphabetically = sort_alphabetically(result)

# Sort the dictionary by frequency (highest to lowest)
sorted_by_frequency = sort_by_frequency(result, reverse=True)

# Sort the dictionary by frequency (lowest to highest)
sorted_by_frequency_low_to_high = sort_by_frequency(result, reverse=False)

print("\nWord frequency in user input:")
for word, frequency in result.items():
    print(f"{word}: {frequency} times")

print("\nWord frequency sorted alphabetically:")
for word, frequency in sorted_alphabetically.items():
    print(f"{word}: {frequency} times")

print("\nWord frequency sorted by frequency (highest to lowest):")
for word, frequency in sorted_by_frequency.items():
    print(f"{word}: {frequency} times")

print("\nWord frequency sorted by frequency (lowest to highest):")
for word, frequency in sorted_by_frequency_low_to_high.items():
    print(f"{word}: {frequency} times")
