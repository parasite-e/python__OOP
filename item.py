import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # validation for received arguments
        assert price >= 0, f"Price, {price} is a negative number!"
        assert quantity >= 0, f"Quantity, {quantity} is a negative number!"

        # assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, value):
        self.__price += self.__price*value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, float):
            return True
        else:
            return False

    def total_price(self):
        return self.__price * self.quantity

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello somebody,
        we have {self.name} {self.quantity} time.         regards.         """ 
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
