from enum import Enum


class PizzaSize(Enum):
    small = 120
    medium = 200
    large = 280

    def __str__(self):
        return self.name

    @property
    def price(self):
        return self.value
        

class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        # if self.size == SMALL:
        #     price = 120 + 20*len(self.toppings)
        # elif self.size == MEDIUM:
        #     price = 200 + 20*len(self.toppings)
        # elif self.size == LARGE:
        #     price = 280 + 20*len(self.toppings)
        # else:
        #     raise ValueError("Unknown pizza size "+self.size)
        # return price
        price = self.size.price + 20*len(self.toppings)
        return price
    
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