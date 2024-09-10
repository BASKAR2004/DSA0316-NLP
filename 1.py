import re

# Example 1: Basic Pattern Matching
text = "The quick brown fox jumps over the lazy dog."
pattern = r'fox'

# Match function - checks if the pattern matches at the start of the string
match = re.match(pattern, text)
if match:
    print("Match found at the beginning of the text!")
else:
    print("No match at the beginning of the text.")

# Search function - searches for the first occurrence of the pattern anywhere in the text
search = re.search(pattern, text)
if search:
    print(f"Pattern found in text: {search.group()}")
else:
    print("Pattern not found in the text.")

# Example 2: Extracting specific parts of a pattern
email_text = "Please contact us at support@example.com for further assistance."
email_pattern = r'(\w+)@(\w+)\.(\w+)'

email_match = re.search(email_pattern, email_text)
if email_match:
    username = email_match.group(1)
    domain = email_match.group(2)
    tld = email_match.group(3)
    print(f"Extracted email components - Username: {username}, Domain: {domain}, TLD: {tld}")

# Example 3: Find all occurrences of a pattern
phone_text = "Call me at 123-456-7890 or 987-654-3210."
phone_pattern = r'\d{3}-\d{3}-\d{4}'

phone_numbers = re.findall(phone_pattern, phone_text)
print(f"Phone numbers found: {phone_numbers}")

# Example 4: Replacing text using regex
text_with_dates = "Today's date is 2024-09-04. Tomorrow's date is 2024-09-05."
date_pattern = r'\d{4}-\d{2}-\d{2}'

# Replace all dates with a generic placeholder
updated_text = re.sub(date_pattern, '[DATE]', text_with_dates)
print(f"Updated text: {updated_text}")

# Example 5: Splitting a string based on a pattern
csv_text = "apple,orange,banana,grape"
split_pattern = r','

fruits = re.split(split_pattern, csv_text)
print(f"Fruits list: {fruits}")
