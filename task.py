class Pizza:
    def get_cost(self): ...
    def get_desctiption(self): ...

class PlainPizza(Pizza):

    def get_cost(self):
        return 5
    def get_desctiption(self):
        return "Plain Dough & Sauce"

class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_cost(self) -> float:
        return self._pizza.get_cost()

    def get_desctiption(self) -> str:
        return self._pizza.get_desctiption()

class Cheese(PizzaDecorator):
    def get_cost(self):
        return super().get_cost() + 2
    def get_desctiption(self):
        return super().get_desctiption() + " + Cheese"

# Olives (+$1), and Pineapple (+$1.5) that can wrap any pizza.
class Olives(PizzaDecorator):
    def get_cost(self):
        return super().get_cost() + 1
    def get_desctiption(self):
        return super().get_desctiption() + " + Olives"

class Pineapple(PizzaDecorator):
    def get_cost(self):
        return super().get_cost() + 1.5
    def get_desctiption(self):
        return super().get_desctiption() + " + Pineapple"

if __name__ == "__main__":

    my_pizza = Pineapple(Olives(Cheese(PlainPizza())))

    print(f"Description: {my_pizza.get_desctiption()}")
    print(f"Total Cost: ${my_pizza.get_cost():.2f}")
