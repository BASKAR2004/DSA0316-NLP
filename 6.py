import random
import nltk
from nltk.util import ngrams
from collections import defaultdict

# Sample text
text = "I love natural language processing. I love machine learning."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Generate bigrams
bigrams = list(ngrams(tokens, 2))

# Build the bigram model
model = defaultdict(list)
for w1, w2 in bigrams:
    model[w1].append(w2)

# Generate text
def generate_text(start_word, num_words):
    current_word = start_word
    sentence = [current_word]
    for _ in range(num_words):
        next_word = random.choice(model[current_word])
        sentence.append(next_word)
        current_word = next_word
    return ' '.join(sentence)

# Example usage
print(generate_text('I', 5))
