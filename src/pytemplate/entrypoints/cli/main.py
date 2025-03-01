from marshmallow import ValidationError
from utils.common import get_choice_input

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder


def main():
    choice = get_choice_input()

    if not isinstance(choice, str):
        raise ValidationError("Invalid input! Please enter a valid burger type.")

    choice = choice.lower()

    try:
        if choice == "chicken":
            return ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        elif choice == "cheese":
            return CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        elif choice == "vegan":
            return VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
        else:
            raise ValidationError(f"Invalid choice: {choice}. Please select 'chicken', 'cheese', or 'vegan'.")

    except ValidationError as err:
        raise ValidationError("Something went wrong") from err

    except Exception as err:
        raise RuntimeError("An unexpected error occurred while creating the burger.") from err
