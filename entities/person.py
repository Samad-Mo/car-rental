from entities.address import Address


class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address
        self.total_money: float = 100

    def deduct_money(self, amount: float) -> None:
        self.total_money -= amount

    def __str__(self):
        return f'{self.name} @ {self.address}'
