from item import Item
from phone import Phone

item1 = Item('cable', 100)
item1.name = 'my item'

item1.apply_increment(0.2)

print(item1.price)

item1.send_email()
