#Cintia Biro-Hajnal 31/10/23
import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Step 1: Read the text file
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

text = read_text_file("own projects\\C371_DA\\4DataProcessingUsingPython\\ASSIGNMENTS\\dataset\\pg84.txt")

# Step 2: Split the text into words
def split_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

words = split_text(text)

# Step 3: Remove stop words
def remove_stop_words(words, stop_words):
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

stop_words = set(stopwords.words('english'))
words_clean = remove_stop_words(words, stop_words)

# Step 4: Lemmatize the words
def lemmatize_words(words_clean):
    lemmatizer = WordNetLemmatizer()
    words_lemmatized = [lemmatizer.lemmatize(word) for word in words_clean]
    return words_lemmatized

words_lemmatized = lemmatize_words(words_clean)

# Step 5: Count the words
def compute_frequency_words(words_lemmatized):
    words_frequency = dict(Counter(words_lemmatized))
    return words_frequency

words_frequency = compute_frequency_words(words_lemmatized)

# Step 6: Export the results to a JSON file
def save_words_frequency(words_frequency, file_path="own projects\\C371_DA\\4DataProcessingUsingPython\\ASSIGNMENTS\\dataset\\words_frequency.json"):
    with open(file_path, 'w') as json_file:
        json.dump(words_frequency, json_file)

save_words_frequency(words_frequency, file_path="own projects\\C371_DA\\4DataProcessingUsingPython\\ASSIGNMENTS\\dataset\\words_frequency.json")
