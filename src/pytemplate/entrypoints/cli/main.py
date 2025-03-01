from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder
from pytemplate.utils.common import get_choice_input


def get_burger_builder(choice):
    """Returns the appropriate burger builder based on the choice."""
    burger_map = {
        "chicken": ChickenBurgerBuilder(),
        "cheese": CheeseBurgerBuilder(),
        "vegan": VeggieBurgerBuilder(),
    }

    if choice not in burger_map:
        raise ValidationError("Invalid choice!")

    return burger_map[choice]


def build_burger(builder):
    """Builds a burger using the builder."""
    return builder.bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()


def main():
    """Main function to get input and create a burger."""
    choice = get_choice_input()
    try:
        builder = get_burger_builder(choice)
        return build_burger(builder)
    except Exception as err:
        raise ValidationError("An unexpected error occurred while creating the burger.") from err
