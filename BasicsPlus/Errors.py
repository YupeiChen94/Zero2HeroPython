# Handle exception thrown by code by using try and except blocks
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('Type error! Watch out!')

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('You cannot divide by zero!')
finally:
    print('All done!')


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block
def ask():
    while True:
        try:
            userinput = int(input('Please input an integer: '))
        except ValueError:
            print('Input was not a number!')
            continue
        else:
            break
    print('Your number squared is: {}'.format(userinput**2))


ask()
