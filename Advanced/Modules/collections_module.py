from collections import Counter, defaultdict, namedtuple

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 'g']
counter_obj = Counter(mylist)
print(Counter(mylist))
print(counter_obj['g'])

letters = 'aaabbbbccccccccd'
c = Counter(letters)
print(c)
# TOP 2 most common
print(c.most_common(2))
# Second most common
print(c.most_common(2)[1])
print(list(c))

d = {'a': 10}
print(d['a'])
# print(d['WRONG'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['WRONG'])

mytuple = (10, 20, 30)
print(mytuple[0])
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
print(Dog)
sammy = Dog(age=5, breed='husky', name='Sam')
print(type(sammy))
print(sammy)
print(sammy.age, sammy.breed, sammy.name)
print(sammy[0], sammy[1], sammy[2])
