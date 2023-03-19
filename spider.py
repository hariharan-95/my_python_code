class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color 
        self.apple_quantity = apple_quantity
    def increase(self):
        self.apple_quantity+=1
    def __str__(self):
        return "A basket of {0} {1} apples.".format(self.apple_quantity, self.apple_color)
        
tmp1=AppleBasket("red",4)
print(tmp1)


class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)


class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, {0}, has {1} dollars.".format(self.name, self.amt)


t1 = BankAccount("Bob", 100)
print(t1)
