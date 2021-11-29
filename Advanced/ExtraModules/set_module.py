# Initialize set
s = set()
# Add objects to set
s.add(1)
s.add(2)
print(s)
# Clear out set
s.clear()
print(s)

s = {1,2,3}
# Make a copy of the  set
sc = s.copy()
s.add(4)
print(sc, s)

# Get difference in set
print(s.difference(sc))

s1, s2 = {1, 2, 3}, {1, 4, 5}
# Remove from s1 the duplicates found in s2
s1.difference_update(s2)
print(s1)

s.discard(4)
print(s)

s1, s2 = {1, 2, 3}, {1, 2, 4}
# Intersection to find duplicates between two sets
print(s1.intersection(s2))

# Update s1 to only include intersections
s1.intersection_update(s2)
print(s1)

s1, s2, s3 = {1, 2}, {1, 2, 4}, {5}
# Returns true if two sets have a null intersection
print(s1.isdisjoint(s2))  # False because these two sets have an intersection of 1 and 2
print(s1.isdisjoint(s3))  # True because there is no intersection
# Is subset
print(s1.issubset(s2))
# Is superset
print(s2.issuperset(s1))

# Symmetric difference finds elements that are not duplicate in two sets
print(s1.symmetric_difference(s2))

# Union returns all element that are in either set
print(s1.union(s2))
# In place union
s1.update(s2)



