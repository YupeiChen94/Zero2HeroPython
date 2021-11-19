def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


# print(create_cubes(10))
# for x in create_cubes(10):
#     print(x)


def create_cubes_generator(n):
    for x in range(n):
        yield x**3


for x in create_cubes_generator(10):
    print(x)

print(list(create_cubes_generator(10)))


def gen_fibbon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


print(list(gen_fibbon(10)))


def simple_gen(n):
    for x in range(n):
        yield x


for number in simple_gen(3):
    print(number)


g = simple_gen(3)

print(g)
print(next(g))
print(next(g))

s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))