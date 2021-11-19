def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() func inside hello!'

    print('I am going to return a function!')
    if name == 'Jose':
        return greet()
    else:
        return welcome()


# my_new_func = hello('Jose')


def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool


# some_func = cool()
# print(some_func())

def hello():
    return 'Hi Jose!'


def other(some_other_func):
    print('Other code runs here!')
    print(some_other_func())


# hello()
# other(hello)


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')

    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!')


# decorated_func = new_decorator(func_needs_decorator())


@new_decorator
def func_needs_decorator2():
    print('I want to be decorated!')


func_needs_decorator2()

