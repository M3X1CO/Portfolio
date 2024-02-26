class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # run validations to the received args
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate          #Item.pay_rate


item1 = Item("Phone", 100, 5)
item1.apply_discount()
print(item1.price)
#print(item1.name)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
#print(item2.name, item2.price, item2.quantity)

#print(item1.calculate_total_price())

#print(Item.__dict__) # creates a dict with attributes for the class level
#print(item1.__dict__) # creates a dict with attributes for the instance level
