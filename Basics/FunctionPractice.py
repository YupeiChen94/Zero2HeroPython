def lesser_of_two_evens(a, b):
    """Write a function that returns the lesser of two given numbers if both numbers are even,
    but returns the greater if one or both numbers are odd"""

    if a % 2 + b % 2 == 0:
        return min(a, b)
    return max(a, b)


# CHECK
print(lesser_of_two_evens(2, 4))  # Return 2
print(lesser_of_two_evens(2, 5))  # Return 5
print(lesser_of_two_evens(7, 5))  # Return 7
print('----------------------------')


def animal_crackers(text):
    """"Write a function that takes a two-word string and returns True if both words begin with the same letter,
    otherwise returns False"""

    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]


# CHECK
print(animal_crackers('Levelheaded Llama'))  # Return True
print(animal_crackers('Crazy Kangaroo'))  # Return False
print(animal_crackers('Crazy cat'))  # Return True
print('----------------------------')


def makes_twenty(a, b):
    """Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not
    return False """
    return (a + b) == 20 or a == 20 or b == 20


# CHECK
print(makes_twenty(20, 10))  # Return True
print(makes_twenty(2, 3))  # Return False
print(makes_twenty(1, 19))  # Return True
print('----------------------------')


def old_macdonald(name):
    """Write a function that capitalizes the first and fourth letters of a name"""
    charlist = list(name.lower())
    newname = ''
    for idx, char in enumerate(charlist):
        if idx in (0, 3):
            newname += char.upper()
        else:
            newname += char
    return newname


# CHECK
print(old_macdonald('macdonald'))  # Return MacDonald
print('----------------------------')


def master_yoda(text):
    """Given a sentence, return a sentence with the words reversed"""
    return ' '.join(text.split()[::-1])


# CHECK
print(master_yoda('I am home'))  # Return home am I
print(master_yoda('We are ready'))  # Return ready we Are
print('----------------------------')


def almost_there(n):
    """Given an integer n, return True if n is within 10 of either 100 or 200"""
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


# CHECK
print(almost_there(104))  # Return True
print(almost_there(150))  # Return False
print(almost_there(209))  # Return True
print('----------------------------')


def has_33(nums):
    """Given a list of ints, return True if the array contains a 3 next to a 3 somewhere"""
    return ''.join(map(str, nums)).find('33') != -1


# CHECK
print(has_33([1, 3, 3]))  # Return True
print(has_33([1, 3, 1, 3]))  # Return False
print(has_33([3, 1, 3]))  # Return False
print('----------------------------')


def paper_doll(text):
    """Given a string, return a string where for every character in the original there are three characters"""
    newtext = ''
    for c in text:
        newtext += c * 3
    return newtext


# CHECK
print(paper_doll('Hello'))  # Return HHHeeellllllooo
print(paper_doll('Mississippi'))  # Return MMMiiissssssiiissssssiiippppppiii
print('----------------------------')


def blackjack(a, b, c):
    """Given 3 ints between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
    If the sum exceeds 21, return BUST."""
    cards = [a, b, c]
    print('Cards: {}'.format(cards))
    if sum(cards) < 22:
        return sum(cards)
    elif 11 in cards:
        cards[cards.index(11)] = 1
        return blackjack(*cards)
    else:
        return 'BUST'


# CHECK
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print('----------------------------')


def summer_69(arr):
    """Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9.
    Return 0 for no numbers"""
    sum = 0
    grab = True
    for n in arr:
        if n == 6:
            grab = False
        if grab:
            sum += n
        if n == 9:
            grab = True
    return sum


# CHECK
print(summer_69([1, 3, 5]))  # Return 9
print(summer_69([4, 5, 6, 7, 8, 9]))  # Return 9
print(summer_69([2, 1, 6, 9, 11]))  # Return 14
print('----------------------------')


def spy_game(ints):
    """Write a function that takes in a list of integers and returns True if it contains 007 in order"""
    ints = [x for x in ints if x in (0, 7)]
    return ''.join(map(str, ints)).find('007') != -1


# CHECK
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Return True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Return True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Return False
print('----------------------------')


def count_primes(n):
    """Write a function that returns the number of prime numbers that exist up to and including a given number"""
    count = 0
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            count += 1
    return count


# CHECK
print(count_primes(100))  # Return 25
print(count_primes(101))  # Return 26
print(count_primes(102))  # Return 26
print('----------------------------')

from math import pi


def vol(rad):
    """Write a function that computes the colume of a sphere given its radius"""
    return 4 / 3 * pi * rad ** 3


# CHECK
print(vol(2))  # Return 33.4933
print('----------------------------')


def ran_check(num, low, high):
    """Check if a number is in a given inclusive range"""
    return num in range(low, high + 1)


# CHECK
print(ran_check(5, 2, 7))  # Return True
print(ran_check(1, 2, 7))  # Return False
print(ran_check(3, 1, 10))  # Return True
print('----------------------------')


def up_low(s):
    """Calculate number of upper and lowercase letters"""
    uppers = len([c for c in s if c.isupper()])
    lowers = len([c for c in s if c.islower()])
    print('Original String: {}'.format(s))
    print('No. of Upper case characters: {}'.format(uppers))
    print('No. of Lower case characters: {}'.format(lowers))
    print('----------------------------')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Return 4 upper, 33 lower


def unique_list(lst):
    """Returns a new list with unique elements of the first list"""
    return list(set(lst))


# CHECK
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))  # Return [1,2,3,4,5]
print('----------------------------')


def multiply(lst):
    """Multiply all the numbers in a list"""
    sum = 1
    for i in lst:
        sum *= i
    return sum


# CHECK
print(multiply([1, 2, 3, -4])) #Return -24
print('----------------------------')


import re
def palindrome(s):
    """Check if word or phrase is palindrome"""
    s = re.sub(r'[^\w]', '', s.lower())
    return s == s[::-1]


# CHECK
print(palindrome('Nurses Run')) #Return True
print(palindrome('ABCEBA')) #Return False
print('----------------------------')


import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    """Check is string is pangram or not (contains every letter of the alphabet)"""
    alphaset = set(alphabet)
    s = set(re.sub(r'[^\w]', '', str1.lower()))
    return s == alphaset


# CHECK
print(ispangram('The quick brown fox jumps over the lazy dog')) #Return True
print(ispangram('I was here')) #Return False
print('----------------------------')
