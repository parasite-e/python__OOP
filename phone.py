from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        super().__init__(name, price, quantity)

        # validation check
        assert broken_phones >= 0, f"Broken Phones {
            broken_phones} is not a valid input"

        # assign to self object
        self.broken_phones = broken_phones
