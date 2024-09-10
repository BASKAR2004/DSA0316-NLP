import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')        # For tokenization
nltk.download('wordnet')      # For lemmatization

# Sample text for morphological analysis
text = "Cats are playing in the garden"

# Step 1: Tokenization - Break the text into individual words
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Step 2: Stemming - Reduce words to their root form using PorterStemmer
stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]
print("Stems:", stems)

# Step 3: Lemmatization - Get the dictionary form of words using WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmas:", lemmas)
