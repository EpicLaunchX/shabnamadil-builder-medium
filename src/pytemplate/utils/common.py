"""Common shared file for supplementary utils"""

from marshmallow import ValidationError


def get_choice_input():
    valid_choices = {"chicken", "vegan", "cheese"}
    try:
        choice = str(input("Please choose a burger type (chicken, vegan, cheese): ")).strip().lower()
        if choice not in valid_choices:
            raise ValidationError("Invalid choice!")
        return choice
    except (EOFError, KeyboardInterrupt) as err:
        raise ValidationError("Input was interrupted. Please try again.") from err
