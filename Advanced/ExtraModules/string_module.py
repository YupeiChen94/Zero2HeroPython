s = 'hello world'

print(s.capitalize())
print(s.upper())
print(s.lower())

print(s.count('o'))
print(s.find('o'))

print(s.center(20, 'z'))

print('hello\thi')
print('hello\thi'.expandtabs())

s = 'hello'
# Is alphanumeric
print(s.isalnum())
# Is number
print(s.isalpha())
# Is all lowercase
print(s.islower())
# Is all spaces?
print(s.isspace())
# Is a title case string
print(s.istitle())
# All is uppercase
print(s.isupper())
# Ends with a certain substring
print(s.endswith('o'))

# Split string at all occurances of delimiter
print(s.split('e'))
# Partition returns head, first sep, and end
print(s.partition('e'))

