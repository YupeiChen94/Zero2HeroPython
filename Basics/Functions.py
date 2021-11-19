# Functions
def say_hello(name='Default'):
    print(f'Hello {name}')


say_hello()


# Functions2
def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)
print(result)

# Tuple Unpacking
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print(item)
for ticker, price in stock_prices:
    print(ticker)

# Tuple Unpacking with Logic
work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


name, hours = employee_check(work_hours)
print(f'{name}, {hours}')


def myfunc(string):
    mylist = list(string.lower())
    newstring = ''
    for idx, char in enumerate(mylist):
        if idx%2 == 0:
            newstring += char.upper()
        else:
            newstring += char
    return newstring


# Lambda, Map, Filter
def square(num):
    return num**2


my_nums = list(range(6))
for item in map(square, my_nums):
    print(item)
print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))


def check_even(num):
    return num%2 == 0


my_nums2 = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, my_nums2)))


print(list(map(lambda num: num ** 2, my_nums2)))
print(list(filter(lambda num: num % 2 == 0, my_nums2)))

print(list(map(lambda name: name[0], names)))
print(list(map(lambda name: name[::-1], names)))