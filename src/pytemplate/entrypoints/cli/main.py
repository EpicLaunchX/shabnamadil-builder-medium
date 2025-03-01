from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder
from pytemplate.utils.common import get_choice_input


def create_burger(choice):
    if choice == "chicken":
        return ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "cheese":
        return CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "vegan":
        return VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    else:
        raise ValidationError("Invalid choice!")


def main():
    choice = get_choice_input()
    try:
        return create_burger(choice)
    except Exception as err:
        raise ValidationError("An unexpected error occurred while creating the burger.") from err
