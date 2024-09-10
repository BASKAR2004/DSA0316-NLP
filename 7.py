import nltk

# Sample text
text = "I love natural language processing."

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform POS tagging
nltk.download('averaged_perceptron_tagger')
pos_tags = nltk.pos_tag(tokens)

# Print the result
print(pos_tags)
