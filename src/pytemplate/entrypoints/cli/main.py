from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder
from pytemplate.utils.common import get_choice_input


def create_burger(builder):
    """Create a burger using the given builder."""
    return builder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()


def main():
    choice = get_choice_input()

    # Map the choice to the appropriate burger builder
    burger_map = {
        "chicken": ChickenBurgerBuilder,
        "cheese": CheeseBurgerBuilder,
        "vegan": VeggieBurgerBuilder,
    }

    try:
        # Get the builder based on user choice or raise error if invalid
        builder = burger_map.get(choice)
        if not builder:
            raise ValidationError("Invalid choice!")

        # Call create_burger with the selected builder
        return create_burger(builder)

    except Exception as err:
        raise ValidationError("An unexpected error occurred while creating the burger.") from err
