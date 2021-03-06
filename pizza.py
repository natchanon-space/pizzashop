from enum import Enum


class PizzaSize(Enum):
    small =  {'base_price': 120, 'topping': 20}
    medium = {'base_price': 200, 'topping': 25}
    large =  {'base_price': 300, 'topping': 30}

    @property
    def price(self):
        return self.value['base_price']
    
    @property
    def topping_price(self):
        return self.value['topping']


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError
        self.size = size
        self.toppings = []

    def get_price(self):
       return self.size.price + self.size.topping_price*len(self.toppings)
    
    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        description = str(self.size)
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain cheeze pizza"
        return description


if __name__ == "__main__":
    # test the PizzaSize enum
    for size in PizzaSize:
        print(size.name, "pizza has price", size.value)