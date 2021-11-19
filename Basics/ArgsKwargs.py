def myfunc(*args):
    print(args)
    return sum(args) - 0.5

print(myfunc(1,2,3,10,50))


def myfunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')


myfunc2(fruit='apple', veggie='lettuce')


def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc3(10,20,30, fruit='orange', food='eggs', animal='dog')