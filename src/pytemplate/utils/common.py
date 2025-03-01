"""Common shared file for supplementary utils"""

from marshmallow import ValidationError

from pytemplate.service.burger import CheeseBurgerBuilder, ChickenBurgerBuilder, VeggieBurgerBuilder


def get_choice_input():
    valid_choices = {"chicken", "vegan", "cheese"}
    try:
        choice = str(input("Please choose a burger type (chicken, vegan, cheese): ")).strip().lower()
        if choice not in valid_choices:
            raise ValidationError("Invalid choice!")
        return choice
    except (EOFError, KeyboardInterrupt) as err:
        raise ValidationError("Input was interrupted. Please try again.") from err


def create_burger(choice):
    if choice == "chicken":
        return ChickenBurgerBuilder().bread("Sesame Seed Bun").patty("Chicken").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "cheese":
        return CheeseBurgerBuilder().bread("Sesame Seed Bun").patty("Beef").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    elif choice == "vegan":
        return VeggieBurgerBuilder().bread("Sesame Seed Bun").patty("Veggie").sauce("Ketchup").toppings(["Lettuce", "Tomato"]).build()
    else:
        raise ValidationError("Invalid choice!")
