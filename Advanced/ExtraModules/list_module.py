# Initialize list
l = [1, 2, 3]
l.append(4)
print(l)

print('Number of tens:', l.count(10))
print('Number of ones:', l.count(1))

# Append v extend
x = [1, 2, 3]
x.append([4, 5])
print('Append:', x)
x = [1, 2, 3]
x.extend([4, 5])
print('Extend:', x)

# Index of object in list
print(l.index(2))

# Insert placing object at specified index
l.insert(2, 'inserted')
print(l)

# Pop removes element in list
ele = l.pop()
print(ele)
l.pop(0)
print(l)

# Remove will remove first instance of element from list
l = [1, 2, 3, 4, 3]
l.remove(3)
print(l)

# Reverse
l.reverse()
print(l)

# Sort
l.sort()
print(l)