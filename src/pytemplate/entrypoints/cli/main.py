from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder
from pytemplate.service.burger import ChickenBurgerBuilder
from pytemplate.service.burger import VeggieBurgerBuilder
from pytemplate.utils.common import get_choice_input


def main():
    choice = get_choice_input()

    try:
        if choice == "chicken":
            return ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        elif choice == "vegan":
            return VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        else:
            return CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Cheese").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()

    except Exception as err:
        raise ValidationError("An unexpected error occurred while creating the burger.") from err
