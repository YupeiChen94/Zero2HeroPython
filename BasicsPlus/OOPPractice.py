class Line:
    """Accept coordinates as a pair of tuples and return the slope and distance of the line."""

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        """distance = (x^2 + b^2)^(0.5)"""
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        """slope = delta y / delta x"""
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return (y2-y1)/(x2-x1)


# CHECK
coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:
    """Accept radius and height, return volume and surface area"""

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * self.radius ** 2


# CHECK
c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())


class Account:
    """Has attributes owner and balance, has methods deposit and withdrawal"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return 'Account owner: {}\nAccount balance: {}'.format(self.owner, self.balance)

    def deposit(self, amount):
        """Add specified amount into balance"""
        self.balance += amount
        print('Deposit Accepted')

    def withdraw(self, amount):
        """Remove specified amount from balance, may not exceed balance"""
        if amount <= self.balance:
            self.balance -= amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# CHECK
acct1 = Account('Jose', 100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
