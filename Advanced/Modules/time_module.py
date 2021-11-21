import time

def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


print(func_one(10))
print(func_two(10))