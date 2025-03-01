from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder
from pytemplate.utils.common import get_choice_input


def main():
    choice = get_choice_input()

    if choice == "chicken":
        burger = ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "cheese":
        burger = CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "vegan":
        burger = VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    else:
        raise ValidationError("Invalid choice!")

    return str(burger)