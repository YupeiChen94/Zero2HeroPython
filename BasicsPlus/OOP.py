# class Dog:
#
#     # Class Object Attribute
#     species = 'mammal'
#
#     def __init__(self, breed, name):
#         # Attributes
#         self.breed = breed
#         self.name = name
#
#     # Operations/Actions: Methods
#     def bark(self, number):
#         print('Woof! My name is {} and the number is {}'.format(self.name, number))
#
#
# my_dog = Dog(breed='Lab', name='Sammy')
# print(type(my_dog))
# print(my_dog.breed)
# print(my_dog.species)
# my_dog.bark(7)


class Circle:
    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.get_circumference())


class Animal:

    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print('I am a dog')

    def eat(self):
        print('I am a dog and eating')

    def bark(self):
        print('Woof!')


mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()


# POLYMORPHISM

class PolyDog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class PolyCat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


niko = PolyDog('niko')
felix = PolyCat('felix')

print(niko.speak())
print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


# Abstraction
class AbstractAnimal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


myanimal = AbstractAnimal('fred')


# myanimal.speak()


class AbsDog(AbstractAnimal):

    def speak(self):
        return self.name + ' says woof!'


fido = AbsDog('fido')
print(fido.speak())


# Special Methods
class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')


b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b