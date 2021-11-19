import math
import random

# help(math)

value = 4.35
# Round down
print(math.floor(value))
# Round up
print(math.ceil(value))

# Constants
print(math.pi)
print(math.inf)
print(math.nan)

# Random numbers
random.seed(101)
print(random.randint(0, 100))

# Sampling from list
mylist = list(range(0, 20))
print(mylist)
print(random.choice(mylist))

# With replacement
print(random.choices(population=mylist, k=10))
# Without replacement
print(random.sample(population=mylist, k=10))

# Shuffle list
random.shuffle(mylist)
print(mylist)

# Uniform distribution
print(random.uniform(a=0, b=100))

# Gaussian distribution
print(random.gauss(mu=0, sigma=1))

