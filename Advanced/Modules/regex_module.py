import re

pattern = 'phone'
text = "The agent's phone number is 408-555-1234. Call Soon!"
text2 = "My phone once, my phone twice"

# Find first match
match = re.search(pattern, text)
print(match)
print(match.start(), match.end())

# Multiple matches
matches = re.findall(pattern, text2)
print(matches)
for match in re.finditer(pattern, text2):
    print(match)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone = re.search(phone_pattern, text)
print(phone.group())
print(phone.group(1))
print(phone.group(2))
print(phone.group(3))

# Searching multiple patterns
match = re.search(r'cat|dog', "The cat is here")
print(match)

# Searching with wildcards
match = re.findall(r'.at', 'The cat in the hat went splat')
print(match)

# Starts with
match = re.findall(r'^\d', '2 is  a number')
print(match)

# Ends with
match = re.findall(r'\d$', 'The number is 2')
print(match)

# Exclusion
phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'
match = re.findall(pattern, phrase)
print(match)
