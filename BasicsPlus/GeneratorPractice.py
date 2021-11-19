import random


def gensquares(n):
    """Create a generator that generates the squares of numbers up to some number n"""
    for num in range(n):
        yield num**2


for x in gensquares(10):
    print(x)

print('\n')


def rand_num(low, high, n):
    """Create a generator that yields 'n' random numbers between a low and a high number that are inputs"""
    for quantity in range(n):
        yield random.randint(low, high)


for num in rand_num(1,10,12):
    print(num)


print('\n')

# Use the iter() function to convert the string into an iterator:
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
