import string

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""

# Step 1: Convert to lowercase
s_lower = s.lower()

# Step 2: Split into words
words = s_lower.split()

# Step 3: Count the number of words
word_count = len(words)

# Step 4: Count distinct words using a set
distinct_words = set(words)
distinct_word_count = len(distinct_words)

# Step 5: Calculate word frequencies
word_freq = {}
for word in words:
    word = word.strip(string.punctuation)
    if word:  # Ignore empty words
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Step 6: Remove punctuation and count words
w_clean = [word.strip(string.punctuation) for word in words if word.strip(string.punctuation)]

# Step 7: Display results
print("Step 1 - Lowercase Text:")
print(s_lower)
print("\nStep 2 - Split into Words:")
print(words)
print("\nStep 3 - Word Count:")
print(word_count)
print("\nStep 4 - Distinct Word Count:")
print(distinct_word_count)
print("\nStep 5 - Word Frequencies:")
print(word_freq)
print("\nStep 6 - Words Without Punctuation:")
print(w_clean)
print(len(w_clean))
