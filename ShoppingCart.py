"""
@author: Francis
Date: 01/09/2022
"""

class Item:
    """
    Class of items in the supermarket
    It has a name and a price
    items should be accessed as 
    object_instance.name and
    object_instance.price where
    object_instance is the name of the
    Item object
    """
    def __init__(self, name='', price=0):
        self.price=price
        self.name=name
        
    #getters/accessors
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    
    #mutators
    def setName(self,name):
        self.name=name
    def setPrice(self, price):
        self.price=price
    
    def __str__(self):
        return(f"name = '{self.name}' price = {self.price}")



class ShoppingCart:
    """
    Class has items bought in a supermarket by a customer.
    Remember the Item class? Yes, those are the items,
    basically name and price. 
    It can only take 10 different items and an increase in the item
    quantity should not be consindered an increase in item count.
    We track the total price of the shopping cart, the total number of 
    items, and the quantity per item.
    """
    items = {}
    def __init__(self):
        self.items={}

    def add(self,item):
        if len(self.items) >= 10:
            "Cart already has 10 items"
            return
        count = 1
        if item in self.items.keys():
            count = self.items.get(item)
            count += 1
        self.items[item] = count


    def total(self):
        summ = 0
        for item in (self.items.keys()):
            summ = summ + (item.price * self.items[item])
        return summ


    def __len__(self):
        lenn = 0
        for item in (self.items.keys()):
            lenn = lenn +  self.items[item]
        return lenn       
   
names = ["pens","books"]
prices = ['500','600']
cart = ShoppingCart()

for i in range(len(names)):
    item = Item(names[i],int(prices[i]))
    
    cart.add(item)
    cart.add(item)
    print(item)

item = Item("Pencils",200)
print(item.name,item.price)

cart.add(item)

print(cart.total())
print(len(cart))


