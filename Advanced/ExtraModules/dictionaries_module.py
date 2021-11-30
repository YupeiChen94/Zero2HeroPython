# Initialize dictionary
d = {'k1': 1, 'k2': 2}

# Dict comprehension
print({x: x**2 for x in range(10)})

# Items
for k in d.items():
    print(k)

# Keys
for k in d.keys():
    print(k)

# Values
for k in d.values():
    print(k)
