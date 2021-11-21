import time
import timeit


def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


# Timing One
start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
# print(elapsed_time)

# Timing Two
start_time = time.time()
result = func_two(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
# print(elapsed_time)

# Using timeit
stmt = '''func_one(100)'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
    '''
print(timeit.timeit(stmt, setup, number=10000))
stmt2 = '''func_two(100)'''
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
    '''
print(timeit.timeit(stmt2, setup2, number=10000))

